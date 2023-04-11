import numpy as np 
import matplotlib.pyplot as plt 
from parameters import *
from pathlib import Path 
import matplotlib.gridspec as gridspec
import scipy as scipy
from scipy import stats

#define plotting parameters
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

############## load data #####################
T = "./10s/"
fig = plt.figure(figsize=(cm2inch(5), cm2inch(3.8)))

############## plot linear case ###############
gs1 = gridspec.GridSpec(8, 1)
gs1.update(top=0.98,bottom=0.2,left=0.1,right=0.94,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0:2,0])
ax2 = plt.subplot(gs1[3:4,0])
ax3 = plt.subplot(gs1[5:8,0])

#10s
T = "./10s/"
v_m      = np.load(T+"vms.npy")
v_m_time = np.load(T+"v_mtime.npy")

cas      = np.load(T+"cas.npy")
ca_time  = np.load(T+"catime.npy")

spike    = np.load(T+"senders.npy")
s_time   = np.load(T+"times.npy")

ax1.plot(v_m_time,v_m,'-',linewidth=.5,color='k')
ax1.plot([-70,130],[-3,-3],'k-',linewidth=1.)
ax1.plot([-70,-70],[-3,7],'k-',linewidth=1.)
ax1.text(40,-5,r"$0.1\ \mathrm{s}$",ha="center",va="top",fontsize=6)
ax1.text(-72,2,r"$10\ \mathrm{mV}$",rotation=90,ha="right",va="center",fontsize=6)

ax2.plot(s_time,spike*0.014,"|",linewidth=1.5,color='#3d5a80',label=r'$10\,\mathrm{s}$')
ax3.plot(ca_time/1000.,cas*10,'-',color='#3d5a80',label=r'$\tau_\mathrm{Ca}=10\,\mathrm{s}$')

#1s
T = "./1s/"
v_m      = np.load(T+"vms.npy")
v_m_time = np.load(T+"v_mtime.npy")

cas      = np.load(T+"cas.npy")
ca_time  = np.load(T+"catime.npy")

spike    = np.load(T+"senders.npy")
s_time   = np.load(T+"times.npy")

ax2.plot(s_time,spike*0.005,"|",linewidth=1.5,color='#ee6c4d',label=r'$1\,\mathrm{s}$')
ax3.plot(ca_time/1000.,cas,'-',color='#ee6c4d',label=r'$\tau_\mathrm{Ca}=1\,\mathrm{s}$')
ax3.set_xlabel("Time (s)")
ax3.set_ylabel(r"$[\mathrm{Ca}^{2+}]_i$")
ax1.set_axis_off()
ax2.set_axis_off()
ax2.set_ylim(0.005,0.014)

for ax in [ax1,ax2,ax3]:
	ax.set_xlim(-74,1000)
	ax3.set_xlim(-0.074,1)
ax3.legend(bbox_to_anchor=(0.11, 0.65, 0.5, 0.5), loc=1,ncol=1, mode="expand", borderaxespad=0.,frameon=False)

ax3.spines['left'].set_position(('data',0))
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')

ax3.spines['bottom'].set_position(('data',0))
ax3.spines['left'].set_smart_bounds(True)
ax3.spines['bottom'].set_smart_bounds(True)
ax3.set_yticks([])
ax3.set_xticks([0,1])
ax3.spines['left'].set_visible(False)


plt.savefig("vm-ca.svg")
plt.show()
