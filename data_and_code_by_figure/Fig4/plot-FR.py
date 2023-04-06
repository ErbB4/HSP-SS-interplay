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



fig = plt.figure(figsize=(cm2inch(2.8), cm2inch(3.5)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.99,bottom=0.25,left=0.18,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])


T = "./"

time_points = np.load(T+"/sampling_time_points.npy")


seed = 0
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_exc       = np.mean(rates_all[:,0:NE],axis=1)
rates_exc_std   = np.std(rates_all[:,0:NE],axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI],axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI],axis=1)

ax1.hist(rates_all[30,0:NE],bins=20,align='left',color='#47ABD8',alpha=1.,label='E')
ax1.hist(rates_all[30,NE:NE+NI],bins=20,color='#D01B1B',histtype='step',alpha=1.,label='I')
ax1.legend(loc='best',frameon=False)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.axvline(x=7.9,ymin=0,ymax=0.5,linestyle='--',color='#ee6c4d',linewidth=0.5)
ax1.axvline(x=7.827,ymin=0,ymax=0.5,linestyle='-',color='#47ABD8',linewidth=0.5)
ax1.set_yticks([2500,5000])
ax1.set_ylim(0,5500)
ax1.set_xlabel("Activity (Hz)")

ax1.set_ylabel("")

plt.savefig("FR.svg")
plt.show()
