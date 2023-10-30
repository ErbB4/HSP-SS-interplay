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
    weights_1 = weights[np.where(sources<1001)] #from subgroup
    weights_2 = weights[np.where(sources>1001)] #from excitatory neurons

    targets_1 = targets[np.where(sources<1001)] #from subgroup
    targets_2 = targets[np.where(sources>1001)] #from excitatory neurons

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
fig = plt.figure(figsize=(cm2inch(10), cm2inch(7.5)))
gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.95,bottom=0.05,left=0.05,right=0.95,hspace=0.2,wspace=0.2)
ax1 = plt.subplot(gs1[0,0],projection='polar') #plot weights from s to s, time1
ax2 = plt.subplot(gs1[0,1],projection='polar') #plot weights from s to s, time2
ax3 = plt.subplot(gs1[0,2],projection='polar') #plot weights from s to s, time3
ax4 = plt.subplot(gs1[1,0],projection='polar') #plot weights from e to s, time1
ax5 = plt.subplot(gs1[1,1],projection='polar') #plot weights from e to e, time2
ax6 = plt.subplot(gs1[1,2],projection='polar') #plot weights from e to s, time3


sources = np.load(T+"sources_"+str(sampling_time_points[18])+".npy")
targets = np.load(T+"targets_"+str(sampling_time_points[18])+".npy")
weights = np.load(T+"weights_"+str(sampling_time_points[18])+".npy")
input_weights_1,input_weights_2,input_weights_3,input_weights_4 = get_weights(sources,targets,weights,500,1500)


N = 100
theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
radii = np.histogram(input_weights_1,bins=N,range=(0.0,0.5))[0]#10 * np.random.rand(N)
width = 0.07#np.pi / 4 * np.histogram(input_weights_2,bins=N,range=(0.05,0.34))[0]
bars = ax1.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.rainbow(r / 10.0))
    bar.set_alpha(0.5)
ax1.set_title("#Synapse: "+str(len(input_weights_1)),fontsize=6.)
print(len(input_weights_1))

radii = np.histogram(input_weights_2,bins=N,range=(0.0,0.5))[0]#10 * np.random.rand(N)
bars = ax4.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.rainbow(r / 10.0))
    bar.set_alpha(0.5)
ax4.set_title("#Synapse: "+str(len(input_weights_2)),fontsize=6.)
print(len(input_weights_2))



sources = np.load(T+"sources_"+str(sampling_time_points[48])+".npy")
targets = np.load(T+"targets_"+str(sampling_time_points[48])+".npy")
weights = np.load(T+"weights_"+str(sampling_time_points[48])+".npy")
input_weights_1,input_weights_2,input_weights_3,input_weights_4 = get_weights(sources,targets,weights,500,1500)

radii = np.histogram(input_weights_1,bins=N,range=(0.0,0.5))[0]#10 * np.random.rand(N)
bars = ax2.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.rainbow(r / 10.0))
    bar.set_alpha(0.5)
ax2.set_title("#Synapse: "+str(len(input_weights_1)),fontsize=6.)
print(len(input_weights_1))

radii = np.histogram(input_weights_2,bins=N,range=(0.0,0.5))[0]#10 * np.random.rand(N)
bars = ax5.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.rainbow(r / 10.0))
    bar.set_alpha(0.5)
ax5.set_title("#Synapse: "+str(len(input_weights_2)),fontsize=6.)
print(len(input_weights_2))


sources = np.load(T+"sources_"+str(sampling_time_points[52])+".npy")
targets = np.load(T+"targets_"+str(sampling_time_points[52])+".npy")
weights = np.load(T+"weights_"+str(sampling_time_points[52])+".npy")
input_weights_1,input_weights_2,input_weights_3,input_weights_4 = get_weights(sources,targets,weights,500,1500)

radii = np.histogram(input_weights_1,bins=N,range=(0.0,0.5))[0]#10 * np.random.rand(N)
bars = ax3.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.rainbow(r / 10.0))
    bar.set_alpha(0.5)
ax3.set_title("#Synapse: "+str(len(input_weights_1)),fontsize=6.)
print(len(input_weights_1))

radii = np.histogram(input_weights_2,bins=N,range=(0.0,0.5))[0]#10 * np.random.rand(N)
bars = ax6.bar(theta, radii, width=width, bottom=0.0)
for r, bar in zip(radii, bars):
    bar.set_facecolor(plt.cm.rainbow(r / 10.0))
    bar.set_alpha(0.5)
ax6.set_title("#Synapse: "+str(len(input_weights_2)),fontsize=6.)
print(len(input_weights_2))

for ax in [ax1,ax2,ax3]:
    ax.set_ylim(0,100)
    ax.set_yticks([0,20,40,60,80,100])
    ax.set_yticklabels(["","20","","60","","100"])
    ax.set_xticks(np.linspace(0.0, 2 * np.pi, 10, endpoint=False))
    ax.set_xticklabels(["0.0 mV"," ","0.1mV"," ","0.2mV","","0.3mV"," ","0.4mV"," "])

for ax in [ax4,ax5,ax6]:
    ax.set_ylim(0,1000)
    ax.set_yticks([0,200,400,600,800,1000])
    ax.set_yticklabels(["","200","","600","","1000"])
    ax.set_xticks(np.linspace(0.0, 2 * np.pi, 10, endpoint=False))
    ax.set_xticklabels(["0.0mV"," ","0.1mV"," ","0.2mV","","0.3mV"," ","0.4mV"," "])

#plt.savefig("weights_and_FR_circular.svg")
plt.show()

