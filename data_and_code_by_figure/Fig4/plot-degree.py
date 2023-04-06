import numpy as np
import matplotlib.pyplot as plt
from parameters import *
from matplotlib import gridspec


####setting for figures####
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=1.5
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

def get_cumulative(data):
    data_sorted = np.sort(data)
    percentile = []
    
    idx = 0
    for item in data_sorted:
        percentile.append((idx+1)/len(data_sorted))
        idx +=1
    return data_sorted,percentile



fig = plt.figure(figsize=(cm2inch(2.8), cm2inch(3.5)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.99,bottom=0.25,left=0.18,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])

def degree(data):
    indegree = np.sum(matrix,axis=0)
    outdegree = np.sum(matrix,axis=1)
    degree_counts = indegree + outdegree
    return degree_counts


seed=0

T = "./"

matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
degree_counts = degree(matrix)
ax1.hist(degree_counts,range=(0,2200),bins=80,histtype="step",color="k")



ax1.set_yticks([])

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

ax1.set_xlabel(r"$\#$ Synapses")
ax1.set_yticks([2500,5000])
ax1.set_xlim(-100,2210)
ax1.set_ylim(0,5500)

plt.savefig("indegree-outdegree.svg")

plt.show()
