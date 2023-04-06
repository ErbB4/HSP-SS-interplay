import numpy as np
from parameters import *
import nest
import matplotlib.pyplot as plt

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



# build network
neuron = nest.Create('excitatory', 1)
poisson_generator = nest.Create("poisson_generator",1,{"rate":10000.})
nest.CopyModel("static_synapse", "device", {"weight":weight, "delay":max_delay})

spike_detector        = nest.Create("spike_detector",1,{"start":0.})
nest.Connect(poisson_generator, neuron, 'all_to_all', syn_spec = "device")
nest.Connect(neuron, spike_detector, 'all_to_all', syn_spec = "device")

m = nest.Create("multimeter",
                params = {"interval": 0.1,
                          "record_from": ["V_m"],
                          "withgid": True,
                          "to_memory": True,
                          "label": "my_multimeter",
                          "start": 0.})
nest.Connect(m, neuron)


                          


cas = []
for time_step in np.arange(0,1000.,dt):
    nest.Simulate(dt)
    ca = nest.GetStatus(neuron,"Ca")
    cas.append(ca[0]) 


#get spike train
events  = nest.GetStatus(spike_detector,'events')[0]
times   = events['times']
senders = events['senders']
np.save("times.npy",times)
np.save("senders.npy",senders)

#get v_m
data = nest.GetStatus(m)[0]['events']
v_m = data['V_m']
time = data['times']

np.save("v_mtime.npy",time)
np.save("vms.npy",v_m)

#save cas
np.save("catime.npy",np.arange(0,1000.,dt))
np.save("cas.npy",cas)


#plot

plt.figure(1)
plt.plot(time,v_m,'-')

plt.figure(2)
plt.plot(np.arange(0,1000.,dt),cas,'-')
plt.plot(times,senders*0.001,"|")
plt.show()
