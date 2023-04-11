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


fig = plt.figure(figsize=(cm2inch(5.5), cm2inch(3.8)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.8,bottom=0.2,left=0.15,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0:2,0])



#10s - 100%rate
T = "./network_simulation/10s-100percent_growth_rate"
seed = 0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
connectivity_ll    = np.load(T+"/connectivity_ll_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,connectivity_ll,'-',color='#3d5a80',label=r'$\tau_\mathrm{Ca}=10\,\mathrm{s}$')

#1s - 100%rate
T = "./network_simulation/1s-100percent_growth_rate"
seed = 0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
connectivity_ll    = np.load(T+"/connectivity_ll_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,connectivity_ll,'-',color='#ee6c4d',label=r'$\tau_\mathrm{Ca}=1\,\mathrm{s}$')

#10s - 10%rate

T = "./network_simulation/10s-10percent_growth_rate"
seed = 2
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
#connectivity_rl    = np.load(T+"/connectivity_rl_seed_"+str(seed)+".npy")
connectivity_ll    = np.load(T+"/connectivity_ll_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,connectivity_ll,'--',color='#98c1d9',label=r'$\mathrm{slow,\ }\tau_\mathrm{Ca}=10\,\mathrm{s}$')
ax1.set_ylabel(r'$\Gamma_{\mathrm{S-S}}$')
ax1.set_xlabel("Time (s)")

ax1.legend(bbox_to_anchor=(0.0, -0.35, 1., 0.1), loc=3,ncol=2, mode="expand", borderaxespad=0.,frameon=False)

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('top')
ax1.xaxis.set_label_position('top')
ax1.spines['bottom'].set_position(('data',0.12))


ax1.set_xlim(5500,8000)
ax1.set_xticks([6000,6500,7000,7500])
ax1.set_xticklabels(["silencing",6500,7000,7500])
ax1.set_yticks([0.,0.05,0.1,0.12])
ax1.set_ylim(-0.01,0.12)
#plt.savefig("conns-zoomedin.svg")
plt.savefig("conns.svg")

plt.show()
