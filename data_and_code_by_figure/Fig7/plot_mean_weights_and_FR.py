import numpy as np 
import matplotlib.pyplot as plt 
from parameters import *
from pathlib import Path 
import matplotlib.gridspec as gridspec
import scipy as scipy
from scipy import stats

#define plotting parameters
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=1.
plt.rcParams["lines.markersize"]=2
plt.rcParams["xtick.labelsize"]=6
plt.rcParams["ytick.labelsize"]=6
plt.rcParams["font.family"] = "arial"
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.rcParams["legend.fontsize"] = 6
plt.rcParams['xtick.minor.width'] = 0.5
plt.rcParams['xtick.major.width'] = 0.5
plt.rcParams['ytick.minor.width'] = 0.5
plt.rcParams['ytick.major.width'] = 0.5

def cm2inch(value):
    #transfer the unit of figure size from cm to inch
    return value/2.54


def get_weights(sources,targets,weights,targetID1,targetID2):
    weights_1 = weights[np.where(sources<1000)]
    weights_2 = weights[np.where(sources>1000)]

    targets_1 = targets[np.where(sources<1000)]
    targets_2 = targets[np.where(sources>1000)]

    input_weights_1 = weights_1[np.where(targets_1==targetID1)]
    input_weights_2 = weights_2[np.where(targets_2==targetID1)]

    input_weights_3 = weights_1[np.where(targets_1==targetID2)]
    input_weights_4 = weights_2[np.where(targets_2==targetID2)]

    return input_weights_1,input_weights_2,input_weights_3,input_weights_4






################# get FR of two neurons ############
T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/with-sandra/alpha2/datafullw/"
sampling_time_points = np.load(T + "sampling_time_points_seed_0.npy")
rates_all = np.load(T+"datafullw002rates_all_seed_0.npy")

rates1 = rates_all[:,500] # sample neuron that will be deprived
rates2 = rates_all[:,1500] # sample neuron that will not be deprived


################### get weights for neuron 500 and neuron 1500 ############

dep_mean_1 = []
dep_std_1  = []

dep_mean_2 = []
dep_std_2  = []


ndep_mean_1 = []
ndep_std_1  = []

ndep_mean_2 = []
ndep_std_2  = []

T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/with-sandra/alpha2/resultsfull002/"

for sampling_time_point in sampling_time_points:
    sources = np.load(T+"sources_"+str(sampling_time_point)+".npy")
    targets = np.load(T+"targets_"+str(sampling_time_point)+".npy")
    weights = np.load(T+"weights_"+str(sampling_time_point)+".npy")

    input_weights_1,input_weights_2,input_weights_3,input_weights_4 = get_weights(sources,targets,weights,500,1500)

    dep_mean_1.append(np.mean(input_weights_1))
    dep_std_1.append(np.std(input_weights_1))

    dep_mean_2.append(np.mean(input_weights_2))
    dep_std_2.append(np.std(input_weights_2))

    ndep_mean_1.append(np.mean(input_weights_3))
    ndep_std_1.append(np.std(input_weights_3))

    ndep_mean_2.append(np.mean(input_weights_4))
    ndep_std_2.append(np.std(input_weights_4))


dep_mean_1 = np.array(dep_mean_1)
dep_std_1  = np.array(dep_std_1)

dep_mean_2 = np.array(dep_mean_2)
dep_std_2  = np.array(dep_std_2)

ndep_mean_1 = np.array(ndep_mean_1)
ndep_std_1  = np.array(ndep_std_1)

ndep_mean_2 = np.array(ndep_mean_2)
ndep_std_2  = np.array(ndep_std_2)



############### define canvas ###########
fig = plt.figure(figsize=(cm2inch(5.3), cm2inch(6.5)))
gs1 = gridspec.GridSpec(5, 1)
gs1.update(top=0.9,bottom=0.1,left=0.2,right=0.99,hspace=0.2,wspace=0.2)
ax1 = plt.subplot(gs1[0:2,0]) #plot FR of two sample neurons
ax2 = plt.subplot(gs1[3:5,0]) # plot weights of neuron 1 and neuron 2


################## plot FR for neuron 1 and neuron 2 ##############


ax1.plot(sampling_time_points/1000.,rates1,color='#666666',label='Neuron 1')
ax1.plot(sampling_time_points/1000.,rates2,color='#47abd8',label='Neuron 2')
ax1.plot(sampling_time_points/1000.,[7.9]*len(sampling_time_points),'--',color='grey',linewidth=0.5)

################## plot weights for neuron 1 ##############
ax2.plot(sampling_time_points/1000,dep_mean_1,'-',color='#666666',label='from S')
ax2.fill_between(sampling_time_points/1000,dep_mean_1-dep_std_1,dep_mean_1+dep_std_1,'-',color='#666666',alpha=0.2,label="")

ax2.plot(sampling_time_points/1000,dep_mean_2,'--',color='#666666',label='from E')
ax2.fill_between(sampling_time_points/1000,dep_mean_2-dep_std_2,dep_mean_2+dep_std_2,color='#666666',alpha=0.2)


################## plot weights for neuron 2 ##############

ax2.plot(sampling_time_points/1000,ndep_mean_1,'-',color='#47abd8')
ax2.fill_between(sampling_time_points/1000,ndep_mean_1-ndep_std_1,ndep_mean_1+ndep_std_1,'-',color='#47abd8',alpha=0.2)

ax2.plot(sampling_time_points/1000,ndep_mean_2,'--',color='#47abd8')
ax2.fill_between(sampling_time_points/1000,ndep_mean_2-ndep_std_2,ndep_mean_2+ndep_std_2,color='#47abd8',alpha=0.2)



ax1.set_ylabel("Activity (Hz)")
ax2.set_ylabel(r"$\bar w$")
ax1.legend(bbox_to_anchor=(0.00,0.9,1., 0.1), loc=3,ncol=2, mode="expand", borderaxespad=0.,frameon=False)
ax2.legend(bbox_to_anchor=(0.0, 0.6,0.5, 0.1), loc=3,ncol=1, mode="expand", borderaxespad=0.,frameon=False)

for ax in [ax1,ax2]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)

    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xlim(5500,7600)

ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_ylim(-1,14)
ax2.set_ylim(0.,0.4)
ax2.set_xticks([6000])
ax2.set_xticklabels(['silencing'])
plt.savefig("weights_and_FR.svg")
plt.show()

