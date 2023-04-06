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

def equalize(matrix,size=50):
    matrix_reduced = np.zeros((int(NE/size),int(NE/size)))
    for i in np.arange(0,int(NE/size),1):
        for j in np.arange(0,int(NE/size),1):
            matrix_reduced[i,j] = np.mean(matrix[i*size:(i+1)*size,j*size:(j+1)*size])
    return matrix_reduced

def plot_matrix(matrix,ax):
    cmap='plasma'
    averagesize=20
    vmin = 0.
    vmax = 0.12

    matrix_reduced = equalize(matrix)
    img = ax.imshow(matrix_reduced,vmin=vmin,vmax=vmax,cmap=cmap,aspect=1)

    if ax==ax7:
        cax = fig.add_axes([0.92,0.15,0.02,0.8])
        cbar = plt.colorbar(img,cax=cax,orientation='vertical')
        cbar.set_ticks([0.,0.06,0.12])        
        cbar.set_ticklabels([r"$0\%$",r"$6\%$",r"$12\%$"])
        cax.yaxis.set_label_position('right')
        cbar.set_label(r"$\Gamma$")
############## load data #####################
T = "./Gaussian/"
N_lesion = N_sub

############## plot stimulation ###############
fig = plt.figure(figsize=(cm2inch(6.), cm2inch(2.5)))
gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.99,bottom=0.2,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[1,0])
ax5 = plt.subplot(gs1[1,1])
ax6 = plt.subplot(gs1[1,2])

fig = plt.figure(figsize=(cm2inch(6.), cm2inch(2)))
gs2 = gridspec.GridSpec(1, 3)
gs2.update(top=0.95,bottom=0.15,left=0.05,right=0.9,hspace=0.15,wspace=0.15)

ax7 = plt.subplot(gs2[0,0])
ax8 = plt.subplot(gs2[0,1])
ax9 = plt.subplot(gs2[0,2])

seed = 12
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

connectivity_ll    = np.load(T+"/connectivity_ss_seed_"+str(seed)+".npy")
connectivity_lr    = np.load(T+"/connectivity_sr_seed_"+str(seed)+".npy")
connectivity_rl    = np.load(T+"/connectivity_rs_seed_"+str(seed)+".npy")
connectivity_rr    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")
matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
connectivity = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,connectivity,'-',color='k')
ax1.plot(time_points/1000.,[.1]*61,'--',color='grey',linewidth=0.5)

ax4.plot(time_points/1000.,connectivity_rr,'-',color='#47abd8',label='E-E')
ax4.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label='S-S')
ax4.plot(time_points/1000.,connectivity_lr,'-',color='#aeaeae',label='S-E')

plot_matrix(matrix,ax7)

############## plot weak deprivation ###############
seed = 10
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

connectivity_ll    = np.load(T+"/connectivity_ss_seed_"+str(seed)+".npy")
connectivity_lr    = np.load(T+"/connectivity_sr_seed_"+str(seed)+".npy")
connectivity_rl    = np.load(T+"/connectivity_rs_seed_"+str(seed)+".npy")
connectivity_rr    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")
matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
connectivity = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax2.plot(time_points/1000.,connectivity,'-',color='k')
ax2.plot(time_points/1000.,[.1]*61,'--',color='grey',linewidth=0.5)

ax5.plot(time_points/1000.,connectivity_rr,'-',color='#47abd8',label=r'$\mathrm{E} \rightarrow \mathrm{E}$')
ax5.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label=r'$\mathrm{S} \rightarrow \mathrm{S}$')
ax5.plot(time_points/1000.,connectivity_lr,'-',color='#aeaeae',label=r'$\mathrm{S} \leftrightarrow \mathrm{E}$')
plot_matrix(matrix,ax8)

############## plot strong deprivation ###############
seed = 0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

connectivity_ll    = np.load(T+"/connectivity_ss_seed_"+str(seed)+".npy")
connectivity_lr    = np.load(T+"/connectivity_sr_seed_"+str(seed)+".npy")
connectivity_rl    = np.load(T+"/connectivity_rs_seed_"+str(seed)+".npy")
connectivity_rr    = np.load(T+"/connectivity_rr_seed_"+str(seed)+".npy")
matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
connectivity = np.load(T+"/connectivity_seed_"+str(seed)+".npy")

ax3.plot(time_points/1000.,connectivity,'-',color='k')
ax3.plot(time_points/1000.,[.1]*61,'--',color='grey',linewidth=0.5)

ax6.plot(time_points/1000.,connectivity_rr,'-',color='#47abd8',label=r'$\mathrm{E} \rightarrow \mathrm{E}$')
ax6.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label=r'$\mathrm{S} \rightarrow \mathrm{S}$')
ax6.plot(time_points/1000.,connectivity_lr,'-',color='#aeaeae',label=r'$\mathrm{S} \leftrightarrow \mathrm{E}$')
ax6.plot(time_points/1000.,[0.]*61,'--',color='grey',linewidth=0.5)

plot_matrix(matrix,ax9)

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])

for ax in [ax4,ax5,ax6]:
    ax.spines['bottom'].set_visible(True)
    ax.set_xticks([6000])

for ax in [ax7,ax8,ax9]:
    ax.set_xticks([])
    ax.set_yticks([])
    ax7.set_xticks([10,110])
    ax7.set_xticklabels(["S","E"])
    ax7.set_yticks([10,110])
    ax7.set_yticklabels(["S","E"])



ax4.set_xticklabels(["stim."])
ax5.set_xticklabels(["depriv."])
ax6.set_xticklabels(["silencing"])

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
    ax.set_xlim(5700,7600)
    ax.set_ylim(-0.01,0.15)



ax1.set_ylabel(r"$\Gamma_\mathrm{overall}$")
ax4.set_ylabel(r"$\Gamma_\mathrm{subs}$")
ax4.legend(bbox_to_anchor=(0.0, 1.2, 2.5, 0.2), loc=1,ncol=3, mode="expand", borderaxespad=0.,frameon=False)

plt.figure(1)
plt.savefig("Gaussian-conn.svg")
plt.figure(2)
plt.savefig("Gaussian-matrices.svg")
plt.show()
