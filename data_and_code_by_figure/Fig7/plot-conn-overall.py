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
fig = plt.figure(figsize=(cm2inch(6), cm2inch(15)))
gs1 = gridspec.GridSpec(2, 3)
gs1.update(top=0.9,bottom=0.15,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax4 = plt.subplot(gs1[1,0])
ax5 = plt.subplot(gs1[1,1])
ax6 = plt.subplot(gs1[1,2])

############## plot exp1 ###############
T = "./no_SS/"
seed = 2
i = seed
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

prefix = ""
func_ll = np.load(T+prefix+"/connectivity_ll_seed_"+str(i)+".npy")
func_lr = np.load(T+prefix+"/connectivity_lr_seed_"+str(i)+".npy")
func_rl = np.load(T+prefix+"/connectivity_rl_seed_"+str(i)+".npy")
func_rr = np.load(T+prefix+"/connectivity_rr_seed_"+str(i)+".npy")
func = np.load(T+prefix+"/connectivity_seed_"+str(i)+".npy")

strc = func
str_ll = func_ll
str_lr = func_lr
str_rl = func_rl
str_rr = func_rr

ax1.plot(time_points/1000.,str_rr,'-',color='#47abd8',label='E-E')
ax1.plot(time_points/1000.,str_ll,'-',color='#666666',label='S-S')
ax1.plot(time_points/1000.,str_rl,'-',color='#aeaeae',label='E-S')
ax1.plot(time_points/1000.,str_lr,':',color='#aeaeae',label='S-E')

ax4.plot(time_points/1000.,func_rr,'-',color='#47abd8')
ax4.plot(time_points/1000.,func_ll,'-',color='#666666')
ax4.plot(time_points/1000.,func_rl,'-',color='#aeaeae')
ax4.plot(time_points/1000.,func_lr,':',color='#aeaeae')

############## plot exp2 ###############
T = "./weak_SS/"
i=0
time_points = np.load(T+"/sampling_time_points_seed_"+str(i)+".npy")

prefix = "datafullw001_2"
func_ll = np.load(T+prefix+"func_ll_seed_"+str(i)+".npy")
func_lr = np.load(T+prefix+"func_lr_seed_"+str(i)+".npy")
func_rl = np.load(T+prefix+"func_rl_seed_"+str(i)+".npy")
func_rr = np.load(T+prefix+"func_rr_seed_"+str(i)+".npy")
func = np.load(T+prefix+"func_seed_"+str(i)+".npy")

str_ll = np.load(T+prefix+"str_ll_seed_"+str(i)+".npy")
str_lr = np.load(T+prefix+"str_lr_seed_"+str(i)+".npy")
str_rl = np.load(T+prefix+"str_rl_seed_"+str(i)+".npy")
str_rr = np.load(T+prefix+"str_rr_seed_"+str(i)+".npy")
strc = np.load(T+prefix+"str_seed_"+str(i)+".npy")

ax2.plot(time_points/1000.,str_rr,'-',color='#47abd8',label='E-E')
ax2.plot(time_points/1000.,str_ll,'-',color='#666666',label='S-S')
ax2.plot(time_points/1000.,str_rl,'-',color='#aeaeae',label='E-S')
ax2.plot(time_points/1000.,str_lr,':',color='#aeaeae',label='S-E')

ax5.plot(time_points/1000.,func_rr,'-',color='#47abd8',label='E-E')
ax5.plot(time_points/1000.,func_ll,'-',color='#666666',label='S-S')
ax5.plot(time_points/1000.,func_rl,'-',color='#aeaeae',label='E-S')
ax5.plot(time_points/1000.,func_lr,':',color='#aeaeae',label='S-E')

############## plot exp3 ###############
T = "./doubled_SS/"
prefix = "datafullw002"

func_ll = np.load(T+prefix+"func_ll_seed_"+str(i)+".npy")
func_lr = np.load(T+prefix+"func_lr_seed_"+str(i)+".npy")
func_rl = np.load(T+prefix+"func_rl_seed_"+str(i)+".npy")
func_rr = np.load(T+prefix+"func_rr_seed_"+str(i)+".npy")
func = np.load(T+prefix+"func_seed_"+str(i)+".npy")

str_ll = np.load(T+prefix+"str_ll_seed_"+str(i)+".npy")
str_lr = np.load(T+prefix+"str_lr_seed_"+str(i)+".npy")
str_rl = np.load(T+prefix+"str_rl_seed_"+str(i)+".npy")
str_rr = np.load(T+prefix+"str_rr_seed_"+str(i)+".npy")
strc = np.load(T+prefix+"str_seed_"+str(i)+".npy")

ax3.plot(time_points/1000.,str_rr,'-',color='#47abd8',label='E-E')
ax3.plot(time_points/1000.,str_ll,'-',color='#666666',label='S-S')
ax3.plot(time_points/1000.,str_rl,'-',color='#aeaeae',label='E-S')
ax3.plot(time_points/1000.,str_lr,':',color='#aeaeae',label='E-S')

ax6.plot(time_points/1000.,func_rr,'-',color='#47abd8')
ax6.plot(time_points/1000.,func_ll,'-',color='#666666')
ax6.plot(time_points/1000.,func_rl,'-',color='#aeaeae')
ax6.plot(time_points/1000.,func_lr,':',color='#aeaeae')

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlim(5700,7600)
    ax.set_ylim(0.05,0.3)
    #ax4.set_ylim(0.05,0.3)
    #ax5.set_ylim(0.05,0.3)
    #ax6.set_ylim(0.05,0.3)

for ax in [ax4,ax5,ax6]:
    ax.spines['bottom'].set_visible(True)
    ax.set_xticks([6000])
    ax.set_xticklabels(["silencing"])

ax1.set_ylabel(r"$\Gamma_\mathrm{struc.}$")
ax4.set_ylabel(r"$\Gamma_\mathrm{effec.}$")
ax1.legend(loc='best', frameon=False)


ax6.plot(6900000./1000.,0.27,marker='v',markeredgecolor='k',markerfacecolor='k')
ax6.text(6900000./1000.,0.29,"t2",fontsize=6.,ha='center',va='bottom')

plt.savefig("conn-overall.svg")
plt.show()
