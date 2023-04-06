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
plt.rcParams["lines.markersize"]=5
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

############## plot seed 2 ###############
fig = plt.figure(figsize=(cm2inch(5.5), cm2inch(4)))
gs1 = gridspec.GridSpec(1, 2)
gs1.update(top=0.95,bottom=0.2,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])

fig = plt.figure(figsize=(cm2inch(5.5), cm2inch(1.5)))
gs2 = gridspec.GridSpec(1, 2)
gs2.update(top=0.95,bottom=0.2,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax3 = plt.subplot(gs2[0,0])
ax4 = plt.subplot(gs2[0,1])

T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/large-network-bg-10s-axon-eta-den-2rules-5seeds/"
seed=2
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_lesion       = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std   = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest       = np.mean(rates_all[:,N_lesion:NE]-14,axis=1)
rates_rest_std   = np.std(rates_all[:,N_lesion:NE]-14,axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI]-22,axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI]-22,axis=1)

connectivity_ll = np.load(T+"connectivity_ss_seed_"+str(seed)+".npy")
connectivity_lr = np.load(T+"connectivity_sr_seed_"+str(seed)+".npy")
connectivity_rl = np.load(T+"connectivity_rs_seed_"+str(seed)+".npy")
connectivity_rr = np.load(T+"connectivity_rr_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,rates_lesion,'-',color='#666666',label='S')
ax1.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax1.plot(time_points/1000.,[7.9]*61,'--',color='#ee6c4d',linewidth=0.5)

ax1.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax1.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax1.plot(time_points/1000.,rates_inh,'-',color='#d01b1b')
ax1.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh[0:len(rates_lesion)]-rates_inh_std[0:len(rates_lesion)],color='#d01b1b',alpha=0.2)

ax3.plot(time_points/1000.,connectivity_rr,'-', color='#47abd8',label='E-E')
ax3.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label='S-S')
ax3.plot(time_points/1000.,connectivity_lr,'-.', color='#aeaeae',label='S-E')
ax3.plot(time_points/1000.,connectivity_rl,':',color='#aeaeae',label='E-S')
ax3.legend(loc='best',frameon=False)


############### plot seed 4 ############
seed=4
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_lesion       = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std   = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest       = np.mean(rates_all[:,N_lesion:NE]-14,axis=1)
rates_rest_std   = np.std(rates_all[:,N_lesion:NE]-14,axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI]-22,axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI]-22,axis=1)

connectivity_ll = np.load(T+"connectivity_ss_seed_"+str(seed)+".npy")
connectivity_lr = np.load(T+"connectivity_sr_seed_"+str(seed)+".npy")
connectivity_rl = np.load(T+"connectivity_rs_seed_"+str(seed)+".npy")
connectivity_rr = np.load(T+"connectivity_rr_seed_"+str(seed)+".npy")

ax2.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax2.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax2.plot(time_points/1000.,[7.9]*61,'--',color='#ee6c4d',linewidth=0.5)
ax2.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax2.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)
ax2.plot(time_points/1000.,rates_inh,'-',color='#d01b1b')
ax2.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh[0:len(rates_lesion)]-rates_inh_std[0:len(rates_lesion)],color='#d01b1b',alpha=0.2)

ax4.plot(time_points/1000.,connectivity_rr,'-', color='#47abd8',label='E-E')
ax4.plot(time_points/1000.,connectivity_ll,'-',color='#666666',label='S-S')
ax4.plot(time_points/1000.,connectivity_lr,'-.', color='#aeaeae',label='S-E')
ax4.plot(time_points/1000.,connectivity_rl,':',color='#aeaeae',label='E-S')

ax1.text(5100,7.9,"S",fontsize=8.,color='k',ha='center',va='center')
ax1.text(5100,7.9-14,"E",fontsize=8.,color='k',ha='center',va='center')
ax1.text(5100,7.9-22,"I",fontsize=8.,color='k',ha='center',va='center')

ax2.plot([5800,6800],[0,0],"-",linewidth=1.,color='k')
ax2.plot([5800,5800],[0,10],"-",linewidth=1.,color='k')

ax3.set_ylabel(r"$\Gamma_\mathrm{subs}$")
############### decoration #######
ax1.set_ylim(-20,10)
ax2.set_ylim(-20,10)

ax3.set_ylim(-0.01,0.11)
ax4.set_ylim(-0.01,0.11)

ax3.plot(time_points/1000.,[0.]*61,'--',color='grey',linewidth=0.5)
ax4.plot(time_points/1000.,[0.]*61,'--',color='grey',linewidth=0.5)


for ax in [ax1,ax2,ax3,ax4]:
	ax.spines['left'].set_visible(False)
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.set_xticks([6000])
	ax.set_yticks([])
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	ax.set_xlim(5500,10000)
	ax.set_xticklabels(["silencing"])

plt.figure(1)
plt.savefig("axon-den-FR.svg")
plt.figure(2)
plt.savefig("axon-den-conn.svg")
plt.show()
