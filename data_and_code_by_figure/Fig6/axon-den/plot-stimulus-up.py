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

############## load data #####################

fig = plt.figure(figsize=(cm2inch(3.2), cm2inch(0.8)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.9,bottom=0.23,left=0.05,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])

############## plot stimulation ###############
T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/large-network-bg-10s-axon-eta-den-2rules-5seeds/"
seed=0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,[1.]*20+[0.]*41,'-',color='k')
ax1.plot(time_points/1000.,[1.]*61,'--',color='grey',linewidth=0.5)
ax1.text(8000,0.1,r"$0\%\ \mathrm{FOI}$",fontsize=6.,ha='center',va='bottom')

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_visible(False)
ax1.spines['bottom'].set_visible(True)

ax1.set_xlim(5500,10000)
ax1.set_ylim(-0.2,1.2)
ax1.set_yticks([])
ax1.set_xticks([6000])
ax1.set_xlabel("Time")
ax1.set_xticklabels(["silencing"])

plt.savefig("stimulus-DA.svg")
plt.show()
