import numpy as np
from parameters import *
import sys
import nest

#get index for array job, if it is an arrayjob. If not an arrayjob, i = 0
i = int(sys.argv[1])
growth_factor = [1,0.5,0.1,0.05,0.01]

#save rank for MPI
rank = nest.Rank()



#set up seed for random number
seed        = 0*6748+7928
grng_seed   = seed
rng_seeds   = range(seed+1,seed+total_num_virtual_procs+1)



#set up NEST kernel
nest.ResetKernel()
nest.EnableStructuralPlasticity()
nest.SetKernelStatus({"resolution": dt, "print_time": False})
nest.SetKernelStatus({
    'structural_plasticity_update_interval' : int(MSP_update_interval/dt),
    'grng_seed'                             : grng_seed,
    'rng_seeds'                             : rng_seeds,
    'total_num_virtual_procs'               : total_num_virtual_procs})
nest.SetDefaults(neuron_model, neuron_params)


# create generic neuron with Axon and Dendrite
nest.CopyModel(neuron_model, 'excitatory')
nest.CopyModel(neuron_model, 'inhibitory')


# growth curves
gc_axon  = {'growth_curve': growth_curve_d, 'z': z0_mean, 'growth_rate': growth_factor[i]*slope*target_rate, 'eps': target_rate, 'eta':0.0007,'continuous': False}
gc_den = {'growth_curve': growth_curve_a, 'z': z0_mean, 'growth_rate': growth_factor[i]*slope*target_rate, 'eps': target_rate, 'eta':0.0007,'continuous': False}


nest.SetDefaults('excitatory', 'synaptic_elements', {'Axon_exc': gc_axon, 'Den_exc': gc_den})

# create synapse models
nest.CopyModel(synapse_model, 'msp_excitatory', {"weight":weight, "delay":max_delay})

# use SetKernelStatus to activate the synapse model
nest.SetKernelStatus({
    "min_delay": min_delay,
    "max_delay": max_delay,
    
    "structural_plasticity_synapses":{
                                'syn_exc':{
                                'model':                 'msp_excitatory',
                                'post_synaptic_element': 'Den_exc',
                                'pre_synaptic_element':  'Axon_exc',
                                },
                                
                                },
    'autapses': False,
})


# build network
pop_exc = nest.Create('excitatory', NE)
pop_inh = nest.Create('inhibitory', NI)

nest.CopyModel("static_synapse", "device", {"weight":weight, "delay":max_delay})

poisson_generator_inh = nest.Create('poisson_generator')
nest.SetStatus(poisson_generator_inh, {"rate": rate})
nest.Connect(poisson_generator_inh, pop_inh,'all_to_all', syn_spec = "device")

poisson_generator_ex = nest.Create('poisson_generator')
nest.SetStatus(poisson_generator_ex, {"rate": rate})
nest.Connect(poisson_generator_ex, pop_exc,'all_to_all', syn_spec = "device")


spike_detector        = nest.Create("spike_detector")
nest.SetStatus(spike_detector,{
                                "withtime"  : True,
                                "withgid"   : True,
                                })


nest.Connect(pop_exc + pop_inh, spike_detector, 'all_to_all', syn_spec = "device")

nest.CopyModel("static_synapse", "inhibitory_synapse", {"weight":-g*weight, "delay":max_delay})
nest.Connect(pop_inh,pop_exc + pop_inh, conn_spec = {'rule': 'fixed_indegree','indegree': CI}, syn_spec = 'inhibitory_synapse')

nest.CopyModel("static_synapse","EI_synapse", {"weight":weight, "delay":max_delay})
nest.Connect(pop_exc,pop_inh, conn_spec = {'rule': 'fixed_indegree','indegree': CE}, syn_spec = 'EI_synapse')


# define simulate functions
def simulate_cicle(growth_steps, step_size, recording_duration):
    count = 0
    for simulation_time in growth_steps:
        nest.SetStatus(spike_detector, {"start": simulation_time+step_size-recording_duration, "stop": simulation_time+step_size})
        nest.Simulate(step_size)

        extension = str(simulation_time+step_size)+'_seed_'+str(i)+"_rank_"+str(rank)+".npy"

        local_connections = nest.GetConnections(pop_exc, pop_exc)
        sources = nest.GetStatus(local_connections,'source')
        targets = nest.GetStatus(local_connections,'target')

        np.save(T+"/data/sources_"+extension,sources)
        np.save(T+"/data/targets_"+extension,targets)
        del local_connections

        events  = nest.GetStatus(spike_detector,'events')[0]
        times   = events['times']
        senders = events['senders']

        np.save(T+"/data/times_"+extension,times)
        np.save(T+"/data/senders_"+extension,senders)
        nest.SetStatus(spike_detector,'n_events',0)
        
        sampling_time_points.append(simulation_time + step_size)
        np.save(T+"/sampling_time_points_seed_"+str(i)+".npy",sampling_time_points)
        count += 1
            
            
# grow network

step_current_generator = nest.Create("step_current_generator")
nest.SetStatus(step_current_generator, {"amplitude_times": trains_time_points_final, "amplitude_values": trains_amplitude_final})
nest.Connect(step_current_generator, pop_exc,'all_to_all', syn_spec = "device")


growth_steps = np.arange(0, 6*growth_time + growth_time,growth_step)
sampling_time_points = []
simulate_cicle(growth_steps, growth_step, long_duration)

#lesion_steps = np.arange(growth_time, growth_time + growth_step, lesion_step)
#simulate_cicle(lesion_steps, lesion_step, short_duration)

#lesion_steps_long = np.arange(growth_time + growth_step, 3*growth_time, growth_step)
#simulate_cicle(lesion_steps_long, growth_step, long_duration)

