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
fig = plt.figure(figsize=(cm2inch(6.5), cm2inch(4.5)))
gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.99,bottom=0.15,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])

ax4 = plt.subplot(gs1[1,0])
ax5 = plt.subplot(gs1[1,1])
ax6 = plt.subplot(gs1[1,2])

############## plot exp1 ###############
T = "./100stimulus_100GR/"
seed = 0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
connectivity_ll    = np.load(T+"/connectivity_ll_seed_"+str(seed)+".npy")
connectivity_lr    = np.load(T+"/connectivity_lr_seed_"+str(seed)+".npy")
connectivity_rl    = np.load(T+"/connectivity_rl_seed_"+str(seed)+".npy")
connectivity_rr    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")
connectivity = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,connectivity,'-',color='k')
ax1.plot(time_points/1000.,[.1]*90,'--',color='grey',linewidth=0.5)

ax4.plot(time_points/1000.,connectivity_rr,'-',color='#47abd8',label='E-E')
ax4.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label='S-S')
ax4.plot(time_points/1000.,connectivity_lr,'-',color='#aeaeae',label='S-E')
ax4.plot(time_points/1000.,[0.]*90,'--',color='grey',linewidth=0.5)

############## plot exp2 ###############
T = "./100stimulus_10GR/"
seed = 2
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
connectivity_ll    = np.load(T+"/connectivity_ll_seed_"+str(seed)+".npy")
connectivity_lr    = np.load(T+"/connectivity_lr_seed_"+str(seed)+".npy")
connectivity_rl    = np.load(T+"/connectivity_rl_seed_"+str(seed)+".npy")
connectivity_rr    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")
connectivity = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax2.plot(time_points/1000.,connectivity,'-',color='k')
ax2.plot(time_points/1000.,[.1]*90,'--',color='grey',linewidth=0.5)

ax5.plot(time_points/1000.,connectivity_rr,'-',color='#47abd8',label='E-E')
ax5.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label='S-S')
ax5.plot(time_points/1000.,connectivity_lr,'-',color='#aeaeae',label='S-E')
ax5.plot(time_points/1000.,[0.]*90,'--',color='grey',linewidth=0.5)

############## plot exp3 ###############
T = "./200stimulus_10GR/"
seed = 2
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
connectivity_ll    = np.load(T+"/connectivity_ll_seed_"+str(seed)+".npy")
connectivity_lr    = np.load(T+"/connectivity_lr_seed_"+str(seed)+".npy")
connectivity_rl    = np.load(T+"/connectivity_rl_seed_"+str(seed)+".npy")
connectivity_rr    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")
connectivity = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax3.plot(time_points/1000.,connectivity,'-',color='k')
ax3.plot(time_points/1000.,[.1]*90,'--',color='grey',linewidth=0.5)

ax6.plot(time_points/1000.,connectivity_rr,'-',color='#47abd8',label='E-E')
ax6.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label='S-S')
ax6.plot(time_points/1000.,connectivity_lr,'-',color='#aeaeae',label='S-E')
ax6.plot(time_points/1000.,[0.]*90,'--',color='grey',linewidth=0.5)
ax4.plot([5800,5900],[0.01,0.01],"-",linewidth=1.,color='k')
ax5.plot([5800,6800],[0.01,0.01],"-",linewidth=1.,color='k')
ax6.plot([5800,6800],[0.01,0.01],"-",linewidth=1.,color='k')

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['bottom'].set_visible(False)

	ax.set_xlim(5700,9000)
	ax.set_ylim(-0.01,0.14)

	ax.set_xticks([])
	ax.set_yticks([])

for ax in [ax4,ax5,ax6]:
	ax.spines['bottom'].set_visible(True)
	ax.set_xticks([6000,7500])
	ax.set_xticklabels(["depriv.","stim."])

ax1.set_ylabel(r"$\Gamma_\mathrm{overall}$")
ax4.set_ylabel(r"$\Gamma_\mathrm{subs}$")
ax6.legend(bbox_to_anchor=(0.5, 1.25, 0.4, 0.4), loc=1,ncol=1, mode="expand", borderaxespad=0.,frameon=False)

ax1.set_title("$\it{Prtcl.\ 1}$")
ax3.set_title("$\it{Prtcl.\ 2}$")

plt.savefig("conn-overall.svg")
plt.show()
