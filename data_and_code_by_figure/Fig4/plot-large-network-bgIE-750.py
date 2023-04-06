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



fig = plt.figure(figsize=(cm2inch(6.5), cm2inch(4)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(2, 4)
gs1.update(top=0.97,bottom=0.15,left=0.185,right=0.99,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0:3])
ax2 = plt.subplot(gs1[1,0:3])
ax3 = fig.add_axes([0.75,0.75,0.2,0.27])


T = "./with_external_current/750pA/"

seed = 0

time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_exc       = np.mean(rates_all[:,0:NE],axis=1)
rates_exc_std   = np.std(rates_all[:,0:NE],axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI],axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI],axis=1)

connectivity    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,rates_exc,'-',color='#47ABD8')
ax1.fill_between(time_points/1000.,rates_exc+rates_exc_std,rates_exc-rates_exc_std,color='#47ABD8',alpha=0.2)
ax1.plot(time_points/1000.,rates_inh,'-',color='#D01B1B')
ax1.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh-rates_inh_std,color='#D01B1B',alpha=0.2)

ax2.plot(time_points/1000.,connectivity,'-',color='k')

ax1.set_ylim(0,10.2)
ax2.set_ylim(0,0.12)
ax1.set_yticks([0.,5.,7.9,10.0])

ax1.set_xticks([])
ax1.set_ylabel("Activity (Hz)")
ax2.set_ylabel(r"$\Gamma$")


ax3.hist(rates_all[-1,0:NE],bins=20,color='#47ABD8',alpha=1.)
ax3.hist(rates_all[-1,NE:NE+NI],bins=20,color='#D01B1B',histtype='step',alpha=1.)
ax3.set_ylim([0,5000])
ax3.set_xlim(0,13)
ax2.set_xlabel("Time (s)")
ax3.axvline(x=7.9,ymin=0,ymax=0.7,linestyle='--',color='#ef476f',linewidth=0.5)
ax3.axvline(x=np.mean(rates_all[-1,0:NE]),ymin=0,ymax=0.7,linestyle='-',color='#47ABD8',linewidth=0.5)
ax3.set_yticks([])


ax4 = ax2.twinx()
ax4.plot(trains_time_points_final/1000.,trains_amplitude_final,'-',color='#b3b3b3ff')
ax4.set_ylim(0,801)
for ax in [ax1,ax3]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	ax3.spines['left'].set_visible(False)


for ax in [ax2]:
	ax.spines['top'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')

for ax in [ax4]:
	ax.spines['top'].set_visible(False)
	ax.yaxis.set_ticks_position('right')
	ax.yaxis.set_label_position('right')
	ax.xaxis.set_ticks_position('bottom')
	ax.tick_params(axis='y', labelcolor='gray',which='both')
	ax.spines['right'].set_color('gray')
	ax.set_ylabel(r"$I_\mathrm{facilitating}\ \mathrm{(pA)}$",color='grey')

ax1.plot(trains_time_points_final[-1]/1000.,9.5,marker='v',markeredgecolor='k',markerfacecolor='k')
ax2.axvspan(xmin=0,xmax=trains_time_points_final[-1]/1000.,color='#e6e6e6ff')

ax4.set_yticks([0,400,800])
plt.savefig("FR-conn-750.svg")
plt.show()
