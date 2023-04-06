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

fig = plt.figure(figsize=(cm2inch(3.2), cm2inch(2)))
gs1 = gridspec.GridSpec(6, 1)
gs1.update(top=0.95,bottom=0.23,left=0.05,right=0.95,hspace=0.15,wspace=0.15)
ax1 = plt.subplot(gs1[0:4,0])
ax2 = plt.subplot(gs1[4,0])
ax3 = plt.subplot(gs1[5,0])


############## plot stimulation ###############
T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/plastic-gaussian-bgIE-10s-lesion-1000"
seed=0
time_points = np.load(T+"/sampling_time_points_seed_"+str(seed)+".npy")

ax1.plot(time_points/1000.,[1.]*20+[0.]*39,'-',color='k')
ax1.plot(time_points/1000.,[1.]*59,'--',color='grey',linewidth=0.5)
ax1.text(7500,0.1,r"$0\%\ \mathrm{FOI}$",fontsize=6.,ha='center',va='bottom')
ax2.plot(time_points/1000.,[0.5]*59,'-',linewidth=3.,color='#a1c5e7')
ax3.plot(time_points[19::]/1000.,[0.5]*40,'-',linewidth=3.,color='#dd7f5a')

for ax in [ax1,ax2,ax3]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['bottom'].set_visible(False)
	ax.set_xlim(5500,9600)
	#ax1.set_ylim(-0.2,1.12)
	#ax2.set_ylim(0,1.)
	#ax3.set_ylim(0,1.)
	ax.set_xticks([])
	ax.set_yticks([])

ax1.set_ylabel("stimulus")
ax3.spines['bottom'].set_visible(True)
ax3.set_xticks([6000])
ax3.set_xlabel("Time")
ax3.set_xticklabels(["silencing"])
ax2.text(9200,0.5,"HSP",fontsize=6.,color="#a1c5e7",va='center',ha='left')
ax3.text(9200,0.5,"scaling",fontsize=6.,color="#dd7f5a",va='center',ha='left')

plt.savefig("stimulus.svg")
plt.show()
