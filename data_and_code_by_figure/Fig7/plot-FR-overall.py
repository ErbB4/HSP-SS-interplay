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
plt.rcParams["lines.markersize"]=1.
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
fig = plt.figure(figsize=(cm2inch(6.), cm2inch(5.)))
gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.9,bottom=0.15,left=0.1,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])

############## plot exp1 ###############
T = "./no_SS/"
seed = 2
i = seed
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

prefix = ""
rates   = np.load(T+prefix+"rates_all_seed_"+str(i)+".npy")
rates_s = np.mean(rates[::,0:N_lesion],axis=1)
rates_e = np.mean(rates[::,N_lesion:NE]-15,axis=1)
rates_i = np.mean(rates[::,NE:NE+NI]-22,axis=1)
rates_s_std = np.std(rates[::,0:N_lesion],axis=1)
rates_e_std = np.std(rates[::,N_lesion:NE]-15,axis=1)
rates_i_std = np.std(rates[::,NE:NE+NI]-22,axis=1)

ax1.plot(time_points/1000.,rates_e,'-',color='#47abd8')
ax1.fill_between(time_points/1000.,rates_e+rates_e_std,rates_e-rates_e_std,color='#47abd8',alpha=0.2)
ax1.plot(time_points/1000.,rates_i,'-',color='#d01b1b')
ax1.fill_between(time_points/1000.,rates_i+rates_i_std,rates_i-rates_i_std,color='#d01b1b',alpha=0.2)
ax1.plot(time_points/1000.,rates_s,'-',color='#666666')
ax1.fill_between(time_points/1000.,rates_s+rates_s_std,rates_s-rates_s_std,color='#666666',alpha=0.2)
ax1.plot(time_points/1000.,[7.9]*len(time_points),'--',color='#ee6c4d',linewidth=0.5)
ax1.plot(time_points/1000.,[0.]*len(time_points),'--',color='grey',linewidth=0.5)
ax1.set_title("w/o scaling")

############## plot exp2 ###############
T = "./weak_SS/"
i=0
time_points = np.load(T+"/sampling_time_points_seed_"+str(i)+".npy")

prefix = "datafullw001_2"
rates   = np.load(T+prefix+"rates_all_seed_"+str(i)+".npy")
rates_s = np.mean(rates[::,0:N_lesion],axis=1)
rates_e = np.mean(rates[::,N_lesion:NE]-15,axis=1)
rates_i = np.mean(rates[::,NE:NE+NI]-22,axis=1)
rates_s_std = np.std(rates[::,0:N_lesion],axis=1)
rates_e_std = np.std(rates[::,N_lesion:NE]-15,axis=1)
rates_i_std = np.std(rates[::,NE:NE+NI]-22,axis=1)

ax2.plot(time_points/1000.,rates_e,'-',color='#47abd8')
ax2.fill_between(time_points/1000.,rates_e+rates_e_std,rates_e-rates_e_std,color='#47abd8',alpha=0.2)
ax2.plot(time_points/1000.,rates_i,'-',color='#d01b1b')
ax2.fill_between(time_points/1000.,rates_i+rates_i_std,rates_i-rates_i_std,color='#d01b1b',alpha=0.2)
ax2.plot(time_points/1000.,rates_s,'-',color='#666666')
ax2.fill_between(time_points/1000.,rates_s+rates_s_std,rates_s-rates_s_std,color='#666666',alpha=0.2)
ax2.plot(time_points/1000.,[7.9]*len(time_points),'--',color='#ee6c4d',linewidth=0.5)
ax2.plot(time_points/1000.,[0.]*len(time_points),'--',color='grey',linewidth=0.5)
ax2.set_title(r"$\rho=0.01$")

############## plot exp3 ###############
T = "./doubled_SS/"
prefix = "datafullw002"
rates   = np.load(T+prefix+"rates_all_seed_"+str(i)+".npy")
rates_s = np.mean(rates[::,0:N_lesion],axis=1)
rates_e = np.mean(rates[::,N_lesion:NE]-15,axis=1)
rates_i = np.mean(rates[::,NE:NE+NI]-22,axis=1)

rates_s_std = np.std(rates[::,0:N_lesion],axis=1)
rates_e_std = np.std(rates[::,N_lesion:NE]-15,axis=1)
rates_i_std = np.std(rates[::,NE:NE+NI]-22,axis=1)

ax3.plot(time_points/1000.,rates_e,'-',color='#47abd8')
ax3.fill_between(time_points/1000.,rates_e+rates_e_std,rates_e-rates_e_std,color='#47abd8',alpha=0.2)
ax3.plot(time_points/1000.,rates_i,'-',color='#d01b1b')
ax3.fill_between(time_points/1000.,rates_i+rates_i_std,rates_i-rates_i_std,color='#d01b1b',alpha=0.2)
ax3.plot(time_points/1000.,rates_s,'-',color='#666666')
ax3.fill_between(time_points/1000.,rates_s+rates_s_std,rates_s-rates_s_std,color='#666666',alpha=0.2)
ax3.plot(time_points/1000.,[7.9]*len(time_points),'--',color='#ee6c4d',linewidth=0.5)
ax3.plot(time_points/1000.,[0.]*len(time_points),'--',color='grey',linewidth=0.5)
ax3.set_title(r"$\rho=0.02$")

ax3.plot([5800,6800],[-20,-20],"-",linewidth=1.,color='k')
ax3.plot([5800,5800],[-20,-15],"-",linewidth=1.,color='k')

for ax in [ax1,ax2,ax3]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)

	ax.set_xlim(5700,7610)
	ax.set_ylim(-21,11)

	ax.set_xticks([])
	ax.set_yticks([])

	ax.set_xticks([6000])
	ax.set_xticklabels(["silencing"])

ax1.text(5200,7.9,"S",fontsize=8.,color='k',ha='center',va='center')
ax1.text(5200,7.9-15,"E",fontsize=8.,color='k',ha='center',va='center')
ax1.text(5200,7.9-22,"I",fontsize=8.,color='k',ha='center',va='center')

ax3.plot(6000000./1000.,10.,marker='v',markeredgecolor='k',markerfacecolor='k')
ax3.plot(6900000./1000.,10.,marker='v',markeredgecolor='k',markerfacecolor='k')
ax3.plot(7500000./1000.,10.,marker='v',markeredgecolor='k',markerfacecolor='k')

ax3.text(6000000./1000.,10.2,"t1",fontsize=6.,ha='center',va='bottom')
ax3.text(6900000./1000.,10.2,"t2",fontsize=6.,ha='center',va='bottom')
ax3.text(7500000./1000.,10.2,"t3",fontsize=6.,ha='center',va='bottom')


plt.savefig("FR_overall.svg")
plt.show()
