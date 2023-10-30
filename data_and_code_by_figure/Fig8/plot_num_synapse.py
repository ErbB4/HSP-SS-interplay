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



def get_weights_reduced(sources,targets,weights,targetID1):
    weights_1 = weights[np.where(sources<1000)]
    weights_2 = weights[np.where(sources>1000)]

    targets_1 = targets[np.where(sources<1000)]
    targets_2 = targets[np.where(sources>1000)]

    input_weights_1 = weights_1[np.where(targets_1==targetID1)]
    input_weights_2 = weights_2[np.where(targets_2==targetID1)]

    return input_weights_1,input_weights_2


def get_num_synapse(sources,targets,weights):

    num_syn_1 = []
    num_syn_2 = []
    for neuron in np.arange(1,1000,1):
        input_weights_1,input_weights_2 = get_weights_reduced(sources,targets,weights,neuron)
        num_syn_1.append(len(input_weights_1))
        num_syn_2.append(len(input_weights_2))
    num_syn_1_mean = np.mean(np.array(num_syn_1))
    num_syn_2_mean = np.mean(np.array(num_syn_2))

    num_syn_1_std = np.std(np.array(num_syn_1))
    num_syn_2_std = np.std(np.array(num_syn_2))

    return num_syn_1_mean,num_syn_2_mean,num_syn_1_std,num_syn_2_std




################# get FR of two neurons ############
T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/with-sandra/alpha2/datafullw/"
sampling_time_points = np.load(T + "sampling_time_points_seed_0.npy")
rates_all = np.load(T+"datafullw002rates_all_seed_0.npy")
'''
################### get weights for neuron 500 and neuron 1500 ############

n1 = []
n2 = []

T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/with-sandra/alpha2/resultsfull002/"

n1_ave = []
n2_ave = []
n1_std = []
n2_std = []

for sampling_time_point in sampling_time_points:
    sources = np.load(T+"sources_"+str(sampling_time_point)+".npy")
    targets = np.load(T+"targets_"+str(sampling_time_point)+".npy")
    weights = np.load(T+"weights_"+str(sampling_time_point)+".npy")

    input_weights_1,input_weights_2,input_weights_3,input_weights_4 = get_weights(sources,targets,weights,500,1500)

    n1.append(len(input_weights_1))
    n2.append(len(input_weights_2))

    num_syn_1_mean,num_syn_2_mean,num_syn_1_std,num_syn_2_std = get_num_synapse(sources,targets,weights)
    n1_ave.append(num_syn_1_mean)
    n2_ave.append(num_syn_2_mean)
    n1_std.append(num_syn_1_std)
    n2_std.append(num_syn_2_std)

    print(sampling_time_point)

n1 = np.array(n1)
n2 = np.array(n2)
n1_ave = np.array(n1_ave)
n2_ave = np.array(n2_ave)
n1_std = np.array(n1_std)
n2_std = np.array(n2_std)
'''

n1 = np.load("n1.npy")
n2 = np.load("n2.npy")
n1_ave = np.load("n1_ave.npy")
n2_ave = np.load("n2_ave.npy")
n1_std = np.load("n1_std.npy")
n2_std = np.load("n2_std.npy")

n1_ave=n1_ave
n2_ave=n2_ave
n1_std=n1_std
n2_std=n2_std
############### define canvas ###########
fig = plt.figure(figsize=(cm2inch(4.3), cm2inch(7.5)))
gs1 = gridspec.GridSpec(3, 1)
gs1.update(top=0.99,bottom=0.05,left=0.2,right=0.99,hspace=0.2,wspace=0.2)
ax1 = plt.subplot(gs1[0:1,0]) #plot FR of two sample neurons
ax2 = plt.subplot(gs1[1:2,0]) # plot weights of neuron 1
ax3 = plt.subplot(gs1[2:3,0]) # plot weights of neuron 2


################## plot s synpases ##############


ax1.plot(sampling_time_points/1000.,n1/n1[19],'-',color='#666666',label='#synapse from S to N1')
ax1.plot(sampling_time_points/1000.,n1_ave/n1_ave[19],'--',color='#666666',label='average')
#ax1.fill_between(sampling_time_points/1000,n1_ave-n1_std,n1_ave+n1_std,'-',color='#666666',alpha=0.2)


################## plot e synapses ##############
ax2.plot(sampling_time_points/1000,n2/n2[19],'-',color='#47abd8',label='#synapse from E to N1')
ax2.plot(sampling_time_points/1000,n2_ave/n2_ave[19],'--',color='#47abd8',label='average')
#ax2.fill_between(sampling_time_points/1000,n2_ave-n2_std,n2_ave+n2_std,'-',color='#47abd8',alpha=0.2)

################## plot total synapses ##############
ax3.plot(sampling_time_points/1000,(n1+n2)/(n1[19]+n2[19]),'-',color='k',label='total # synapse to N1')
ax3.plot(sampling_time_points/1000,(n1_ave+n2_ave)/(n1_ave[19]+n2_ave[19]),'--',color='k',label='average')
#ax3.fill_between(sampling_time_points/1000,(n1_ave+n2_ave)-(n1_std+n2_std),(n1_ave+n2_ave)+(n1_std+n2_std),'-',color='#47abd8',alpha=0.2)


ax1.legend(bbox_to_anchor=(0.00,0.65,0.6, 0.1), loc=3,ncol=1, mode="expand", borderaxespad=0.,frameon=False)
ax2.legend(bbox_to_anchor=(0.0, 0.55,0.6, 0.1), loc=3,ncol=1, mode="expand", borderaxespad=0.,frameon=False)
ax3.legend(bbox_to_anchor=(0.0, 0.55,0.6, 0.1), loc=3,ncol=1, mode="expand", borderaxespad=0.,frameon=False)

ax3.plot(sampling_time_points[18]/1000.,0.15,marker='v',markeredgecolor='k',markerfacecolor='k')
ax3.plot(sampling_time_points[52]/1000.,0.395,marker='v',markeredgecolor='k',markerfacecolor='k')


for ax in [ax1,ax2,ax3]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xlim(5500,7600)
    ax.set_ylabel("# synapses (%)")

ax1.set_xticks([6000])
ax1.set_xticklabels(['silencing'])
ax1.set_ylim(0.85,1.15)
ax2.set_ylim(0.85,1.15)
ax2.set_xticks([6000])
ax2.set_xticklabels(['silencing'])
ax3.set_ylim(0.85,1.15)
ax3.set_xticks([6000])
ax3.set_xticklabels(['silencing'])
plt.savefig("num_syn.svg")
plt.show()

