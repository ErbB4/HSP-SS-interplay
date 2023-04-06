import numpy as np 
import matplotlib.pyplot as plt 
from parameters import *
from pathlib import Path 
import matplotlib.gridspec as gridspec
import scipy as sp
from scipy import stats

#define plotting parameters
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=2.
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



fig = plt.figure(figsize=(cm2inch(2.8), cm2inch(2.8)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.95,bottom=0.05,left=0.05,right=0.85,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])


T = "./"

time_points = np.load(T+"/sampling_time_points.npy")


seed = 0
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)

rates_step = rates_all[30,0:NE]

def degree(data):
    indegree = np.sum(matrix,axis=0)
    outdegree = np.sum(matrix,axis=1)
    degree_counts = indegree + outdegree
    return degree_counts

T = "./"

matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
degree_counts = degree(matrix)

heatmap, xedges, yedges = np.histogram2d(rates_step, degree_counts, bins=20)
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]


img = ax1.imshow(heatmap.T, extent=extent, vmin=0,vmax=4000,origin='lower',aspect='auto',cmap='Reds')

cax = fig.add_axes([0.89,0.05,0.02,0.9])
cbar = plt.colorbar(img,cax=cax,orientation='vertical')
cbar.set_ticks([0,2000,4000])
cax.yaxis.set_label_position('left')

ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')


ax1.set_xlabel("Activity (Hz)")
ax1.set_ylabel(r"$\#$ Synapses")

plt.savefig("FR-degree.svg")

plt.show()


