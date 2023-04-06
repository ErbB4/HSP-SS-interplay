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
fig = plt.figure(figsize=(cm2inch(6.5), cm2inch(10.)))
gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.99,bottom=0.08,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])


############## plot exp1 ###############
T = "./100stimulus_100GR/"
seed = 0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
rates_all = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all = np.array(rates_all)
rates_lesion = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest = np.mean(rates_all[:,N_lesion:NE]-18,axis=1)
rates_rest_std = np.std(rates_all[:,N_lesion:NE]-18,axis=1)
rates_inh = np.mean(rates_all[:,NE:NE+NI]-30,axis=1)
rates_inh_std = np.std(rates_all[:,NE:NE+NI]-30,axis=1)

ax1.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax1.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax1.plot(time_points/1000.,[7.9]*90,'--',color='#ee6c4d',linewidth=0.5)

ax1.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax1.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax1.plot(time_points/1000.,rates_inh,'-',color='#d01b1b')
ax1.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh-rates_inh_std,color='#d01b1b',alpha=0.2)

############## plot exp2 ###############
T = "./100stimulus_10GR/"
seed = 2
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_lesion       = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std   = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest       = np.mean(rates_all[:,N_lesion:NE]-18,axis=1)
rates_rest_std   = np.std(rates_all[:,N_lesion:NE]-18,axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI]-30,axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI]-30,axis=1)

ax2.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax2.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax2.plot(time_points/1000.,[7.9]*90,'--',color='#ee6c4d',linewidth=0.5)

ax2.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax2.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax2.plot(time_points/1000.,rates_inh,'-',color='#d01b1b')
ax2.fill_between(time_points/1000.,rates_inh+rates_inh_std,rates_inh[0:len(rates_lesion)]-rates_inh_std[0:len(rates_lesion)],color='#d01b1b',alpha=0.2)

############## plot exp3 ###############
T = "./200stimulus_10GR/"
seed = 2
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")
rates_all       = np.load(T+"/rates_all_seed_"+str(seed)+".npy")
rates_all       = np.array(rates_all)
rates_lesion       = np.mean(rates_all[:,0:N_lesion],axis=1)
rates_lesion_std   = np.std(rates_all[:,0:N_lesion],axis=1)
rates_rest       = np.mean(rates_all[:,N_lesion:NE]-18,axis=1)
rates_rest_std   = np.std(rates_all[:,N_lesion:NE]-18,axis=1)
rates_inh       = np.mean(rates_all[:,NE:NE+NI]-30,axis=1)
rates_inh_std   = np.std(rates_all[:,NE:NE+NI]-30,axis=1)

ax3.plot(time_points/1000.,rates_lesion,'-',color='#666666')
ax3.fill_between(time_points/1000.,rates_lesion+rates_lesion_std,rates_lesion-rates_lesion_std,color='#666666',alpha=0.2)
ax3.plot(time_points/1000.,[7.9]*90,'--',color='#ee6c4d',linewidth=0.5)

ax3.plot(time_points/1000.,rates_rest,'-',color='#47abd8')
ax3.fill_between(time_points/1000.,rates_rest+rates_rest_std,rates_rest-rates_rest_std,color='#47abd8',alpha=0.2)

ax3.plot(time_points/1000.,rates_inh[0:len(rates_lesion)],'-',color='#d01b1b')
ax3.fill_between(time_points/1000.,rates_inh[0:len(rates_lesion)]+rates_inh_std[0:len(rates_lesion)],rates_inh[0:len(rates_lesion)]-rates_inh_std[0:len(rates_lesion)],color='#d01b1b',alpha=0.2)

ax1.plot([5800,5900],[-17,-17],"-",linewidth=1.,color='k')
ax1.plot([5800,5800],[-17,-7],"-",linewidth=1.,color='k')

ax2.plot([5800,6800],[-17,-17],"-",linewidth=1.,color='k')
ax2.plot([5800,5800],[-17,-7],"-",linewidth=1.,color='k')

ax3.plot([5800,6800],[-17,-17],"-",linewidth=1.,color='k')
ax3.plot([5800,5800],[-17,-7],"-",linewidth=1.,color='k')

for ax in [ax1,ax2,ax3]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)

	ax.set_xlim(5700,9000)
	#ax.set_ylim(-30,20)
	ax.set_ylim(-30,90)


	ax.set_xticks([])
	ax.set_yticks([])

	ax.set_xticks([6000,7500])
	ax.set_xticklabels(["depriv.","stim."])

ax1.text(5200,7.9,"S",fontsize=8.,color='k',ha='center',va='center')
ax1.text(5200,7.9-18,"E",fontsize=8.,color='k',ha='center',va='center')
ax1.text(5200,7.9-30,"I",fontsize=8.,color='k',ha='center',va='center')

ax1.set_title("$\it{Prtcl.\ 1}$")
ax3.set_title("$\it{Prtcl.\ 2}$")

plt.savefig("FR-overall.svg")
plt.show()
