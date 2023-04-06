import numpy as np
import pylab as pl
from parameters import *
import sys
import h5py as h5

#get index for arrayjob. if not arrayjob, i = 0
i = int(sys.argv[1])


def analysis_rate(senders,times,recording_duration):
    rates = []

    for neuron in np.arange(0,NE+NI,1):
        idx = np.where(senders==neuron+1)
        time = times[idx]
        rate = len(time)/(recording_duration/1000.)
        rates.append(rate)
    return rates

def connectivity_reconsrtuction(sources,targets,NE):
    connectivity_matrix = np.zeros((NE,NE))
    
    sourceIDs = np.unique(sources)
    for sourceID in sourceIDs:
        share_source = targets[np.where(sources==sourceID)]
        targetIDs = np.unique(share_source)
        for targetID in targetIDs:
            same_target = share_source[np.where(share_source==targetID)]
            connectivity_matrix[sourceID-1,targetID-1] = len(same_target)
    return connectivity_matrix


#collect spiking raw data in hdf5 file
sampling_time_points = np.load(T+"/sampling_time_points_seed_"+str(i)+".npy")
diff = np.diff(sampling_time_points)

rates_all = []

connectivity_ll = []
connectivity_lr = []
connectivity_rl = []
connectivity_rr = []
connectivity    = [] 


for counter, time_points in enumerate(sampling_time_points):
    senders = np.array([])
    times   = np.array([])

    sources = np.array([])
    targets = np.array([])

    for rank in np.arange(n_rank):
        senders = np.concatenate((senders, np.load(T+"data/senders_"+str(time_points)+'_seed_'+str(i)+'_rank_'+str(rank)+".npy",allow_pickle=True)))
        times   = np.concatenate((times,   np.load(T+"data/times_"  +str(time_points)+'_seed_'+str(i)+'_rank_'+str(rank)+".npy",allow_pickle=True)))

        sources = np.concatenate((sources, np.load(T+"data/sources_"+str(time_points)+'_seed_'+str(i)+'_rank_'+str(rank)+".npy",allow_pickle=True)))
        targets = np.concatenate((targets, np.load(T+"data/targets_"+str(time_points)+'_seed_'+str(i)+'_rank_'+str(rank)+".npy",allow_pickle=True)))

    if counter == 0:
        rates   = analysis_rate(senders,times,long_duration)
        rates_all.append(rates)
        del rates    	

    else: 
        if diff[counter-1] == growth_step:
            rates   = analysis_rate(senders,times,long_duration)
            rates_all.append(rates)
            del rates

        if diff[counter-1] == lesion_step:
            rates   = analysis_rate(senders,times,short_duration)
            rates_all.append(rates)
            del rates

    sources = sources.astype(int)
    targets = targets.astype(int)
    connectivity_matrix = connectivity_reconsrtuction(sources,targets,NE)

    connectivity_ll.append(np.mean(connectivity_matrix[0:N_lesion,0:N_lesion]))
    connectivity_lr.append(np.mean(connectivity_matrix[0:N_lesion,N_lesion::]))
    connectivity_rl.append(np.mean(connectivity_matrix[N_lesion::,0:N_lesion]))
    connectivity_rr.append(np.mean(connectivity_matrix[N_lesion::,N_lesion::]))
    connectivity.append(np.mean(connectivity_matrix))

    np.save(T+"rates_all_seed_"+str(i)+".npy",rates_all)
    np.save(T+"connectivity_ll_seed_"+str(i)+".npy",connectivity_ll)
    np.save(T+"connectivity_lr_seed_"+str(i)+".npy",connectivity_lr)
    np.save(T+"connectivity_rl_seed_"+str(i)+".npy",connectivity_rl)
    np.save(T+"connectivity_rr_seed_"+str(i)+".npy",connectivity_rr)
    np.save(T+"connectivity_seed_"+str(i)+".npy",connectivity)

