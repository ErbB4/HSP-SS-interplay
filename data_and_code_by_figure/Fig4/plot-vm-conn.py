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


#get conn
T0 = "./"
T1 = "./with_external_current/200pA/"
T2 = "./with_external_current/500pA/"
T3 = "./with_external_current/750pA/"

conn0 = np.load(T0+"connectivity_seed_0.npy")
conn1 = np.load(T1+"connectivity_seed_0.npy")
conn2 = np.load(T2+"connectivity_seed_0.npy")
conn3 = np.load(T3+"connectivity_rr_seed_0.npy")


fig = plt.figure(figsize=(cm2inch(4.), cm2inch(2.3)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.95,bottom=0.15,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
Vs = np.array([0,200,500,750])

ax1.plot(Vs,[conn0[-1],conn1[-1],conn2[-1],conn3[-1]],'ko-')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

ax1.set_xlabel(r"$I_\mathrm{facilitating}\ \mathrm{(pA)}$")
ax1.set_ylabel(r"$\Gamma_\mathrm{equi.}$")
ax1.set_ylim(0,0.11)
plt.savefig("equi.svg")

plt.show()