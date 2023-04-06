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
T = "./Gaussian/"
N_lesion = N_sub

fig = plt.figure(figsize=(cm2inch(6.0), cm2inch(2.)))
gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.85,bottom=0.2,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])

fig = plt.figure(figsize=(cm2inch(6.0), cm2inch(3)))
gs2 = gridspec.GridSpec(1, 3)
gs2.update(top=0.99,bottom=0.2,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax4 = plt.subplot(gs2[0,0])
ax5 = plt.subplot(gs2[0,1])
ax6 = plt.subplot(gs2[0,2])

############## plot stimulation ###############
seed = 12
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
rates_all = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all = np.array(rates_all)
rates_lesion = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest = np.mean(rates_all[:,N_lesion:NE]-12,axis=1)
rates_rest_std = np.std(rates_all[:,N_lesion:NE]-12,axis=1)
rates_inh = np.mean(rates_all[:,NE:NE+NI]-20,axis=1)
rates_inh_std = np.std(rates_all[:,NE:NE+NI]-20,axis=1)

ax1.plot(time_points/1000.,[1.]*20+[1.1]*41,'-',color='k')
ax1.plot(time_points/1000.,[1.]*61,'--',color='grey',linewidth=0.5)
ax1.text(6750,0.8,r"$110\%\ \mathrm{FOI}$",fontsize=6.,ha='center',va='top')

ax4.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax4.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax4.plot(time_points/1000.,[7.9]*len(time_points),'--',color='#ee6c4d',linewidth=0.5)

ax4.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax4.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax4.plot(time_points/1000.,rates_inh,'-',color='#d01b1b')
ax4.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh-rates_inh_std,color='#d01b1b',alpha=0.2)

############## plot weak deprivation ###############
seed = 10
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_lesion       = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std   = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest       = np.mean(rates_all[:,N_lesion:NE]-12,axis=1)
rates_rest_std   = np.std(rates_all[:,N_lesion:NE]-12,axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI]-20,axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI]-20,axis=1)

ax2.plot(time_points/1000.,[1.]*20+[0.95]*41,'-',color='k')
ax2.plot(time_points/1000.,[1.]*61,'--',color='grey',linewidth=0.5)
ax2.text(6750,0.85,r"$95\%\ \mathrm{FOI}$",fontsize=6.,ha='center',va='top')

ax5.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax5.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax5.plot(time_points/1000.,[7.9]*len(time_points),'--',color='#ee6c4d',linewidth=0.5)

ax5.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax5.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax5.plot(time_points/1000.,rates_inh,'-',color='#d01b1b')
ax5.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh[0:len(rates_lesion)]-rates_inh_std[0:len(rates_lesion)],color='#d01b1b',alpha=0.2)

############## plot strong deprivation ###############
seed = 0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_lesion       = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std   = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest       = np.mean(rates_all[:,N_lesion:NE]-12,axis=1)
rates_rest_std   = np.std(rates_all[:,N_lesion:NE]-12,axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI]-20,axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI]-20,axis=1)

ax3.plot(time_points/1000.,[1.]*20+[0.]*41,'-',color='k')
ax3.plot(time_points/1000.,[1.]*61,'--',color='grey',linewidth=0.5)
ax3.text(6750,0.4,r"$0\%\ \mathrm{FOI}$",fontsize=6.,ha='center',va='top')

ax6.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax6.plot(time_points/1000.,[7.9]*len(time_points),'--',color='#ee6c4d',linewidth=0.5)
ax6.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)

ax6.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax6.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax6.plot(time_points/1000.,rates_inh[0:len(rates_lesion)],'-',color='#d01b1b')
ax6.fill_between(time_points/1000.,rates_inh[0:len(rates_lesion)]+rates_inh_std[0:len(rates_lesion)],rates_inh[0:len(rates_lesion)]-rates_inh_std[0:len(rates_lesion)],color='#d01b1b',alpha=0.2)

ax4.plot([5800,6800],[-17,-17],"-",linewidth=1.,color='k')
ax4.plot([5800,5800],[-17,-7],"-",linewidth=1.,color='k')

for ax in [ax1,ax2,ax3,ax4,ax5,ax6]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)

	ax.set_xlim(5700,7610)
	ax.set_ylim(-22,22)

	ax1.set_ylim(-0.1,1.12)
	ax2.set_ylim(-0.1,1.12)
	ax3.set_ylim(-0.1,1.12)

	ax.set_xticks([])
	ax.set_yticks([])

	ax.set_xticks([6000])
	ax2.set_xlabel("Time")

ax1.set_xticklabels(["stim."])
ax2.set_xticklabels(["depriv."])
ax3.set_xticklabels(["silencing"])

ax4.set_xticklabels(["stim."])
ax5.set_xticklabels(["depriv."])
ax6.set_xticklabels(["silencing"])


ax1.set_ylabel("Stimulus")
ax4.text(5200,7.9,"S",fontsize=8.,color='k',ha='center',va='center')
ax4.text(5200,7.9-12,"E",fontsize=8.,color='k',ha='center',va='center')
ax4.text(5200,7.9-20,"I",fontsize=8.,color='k',ha='center',va='center')


ax1.set_title("$\it{stim.}$")
ax2.set_title("$\it{depriv.}$")
ax3.set_title("$\it{silencing}$")

plt.figure(1)
plt.savefig("Gaussian-stimulus.svg")
plt.figure(2)
plt.savefig("Gaussian-FR.svg")
plt.show()
