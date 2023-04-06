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



fig = plt.figure(figsize=(cm2inch(11), cm2inch(4.)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.9,bottom=0.2,left=0.12,right=0.95,hspace=0.05,wspace=0.15)

ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[1,0])
#ax3 = fig.add_axes([0.28,0.648,0.1,0.1])


T = "./plastic-linear/"

time_points = np.load(T+"/sampling_time_points.npy")


seed = 0
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_exc       = np.mean(rates_all[:,0:NE],axis=1)
rates_exc_std   = np.std(rates_all[:,0:NE],axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI],axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI],axis=1)

connectivity    = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,rates_exc,'-',color='#47ABD8',label='E')
ax1.fill_between(time_points/1000.,rates_exc+rates_exc_std,rates_exc-rates_exc_std,color='#47ABD8',alpha=0.2)
ax1.plot(time_points/1000.,rates_inh,'-',color='#D01B1B',label='I')
ax1.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh-rates_inh_std,color='#D01B1B',alpha=0.2)
ax1.plot(time_points[30]/1000.,9.3,marker='v',markeredgecolor='k',markerfacecolor='k')
ax2.plot(time_points/1000.,connectivity,'-',color='k')

ax1.set_ylim(0,10)
ax2.set_ylim(0,0.12)
	
ax1.set_xticks([])
ax1.set_yticks([0.,5.,7.9,10.0])

ax1.set_ylabel("Activity (Hz)")
ax2.set_ylabel(r"$\Gamma$")


############## plot gaussian case ###############

ax4 = plt.subplot(gs1[0,1])
ax5 = plt.subplot(gs1[1,1])
#ax6 = fig.add_axes([0.6,0.648,0.1,0.1])


T = "./plastic-gaussian-0eta/"

time_points = np.load(T+"/sampling_time_points.npy")


seed = 0
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_exc       = np.mean(rates_all[:,0:NE],axis=1)
rates_exc_std   = np.std(rates_all[:,0:NE],axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI],axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI],axis=1)

connectivity    = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax4.plot(time_points/1000.,rates_exc,'-',color='#47ABD8')
ax4.fill_between(time_points/1000.,rates_exc+rates_exc_std,rates_exc-rates_exc_std,color='#47ABD8',alpha=0.2)
ax4.plot(time_points/1000.,rates_inh,'-',color='#D01B1B')
ax4.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh-rates_inh_std,color='#D01B1B',alpha=0.2)
ax4.plot(time_points[30]/1000.,9.3,marker='v',markeredgecolor='k',markerfacecolor='k')

ax5.plot(time_points/1000.,connectivity,'-',color='k')

ax4.set_ylim(0,10)
ax5.set_ylim(0,0.12)
ax4.set_xticks([])
ax5.set_xlabel("Time (s)")
ax4.set_yticks([])
ax5.set_yticks([])



############## plot gaussian case eta>0 ###############

ax7 = plt.subplot(gs1[0,2])
ax8 = plt.subplot(gs1[1,2])
#ax9 = fig.add_axes([0.85,0.44,0.1,0.1])

T = "./plastic-gaussian/"

time_points = np.load(T+"/sampling_time_points.npy")


seed = 0
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_exc       = np.mean(rates_all[:,0:NE],axis=1)
rates_exc_std   = np.std(rates_all[:,0:NE],axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI],axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI],axis=1)

connectivity    = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax7.plot(time_points/1000.,rates_exc,'-',color='#47ABD8',label='E')
ax7.fill_between(time_points/1000.,rates_exc+rates_exc_std,rates_exc-rates_exc_std,color='#47ABD8',alpha=0.2)
ax7.plot(time_points/1000.,rates_inh,'-',color='#D01B1B',label='I')
ax7.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh-rates_inh_std,color='#D01B1B',alpha=0.2)
ax7.plot(time_points[30]/1000.,7.3,marker='v',markeredgecolor='k',markerfacecolor='k')

ax8.plot(time_points/1000.,connectivity,'-',color='k')

ax7.set_ylim(0,10)
ax8.set_ylim(0,0.12)
	
ax7.set_xticks([])
ax1.legend(bbox_to_anchor=(0.2, 0.2, 0.8, 0.2), loc=1,ncol=2, mode="expand", borderaxespad=0.,frameon=False)

ax7.set_yticks([])
ax8.set_yticks([])


for ax in [ax1,ax2,ax4,ax5,ax7,ax8]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')

plt.savefig("three-growth.svg")
plt.show()
