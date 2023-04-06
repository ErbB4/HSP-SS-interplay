import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path 
import matplotlib.gridspec as gridspec
import scipy as scipy
from scipy import stats

from scipy.integrate import simpson
from numpy import trapz

#define plotting parameters
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=1.
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


def get_strc_diff(gf,sf):
    T = "C://Users/han/Desktop/GaussianHSP-SC/with-sandra/alpha2/datafullw/paramspace/"
    time_points = np.load(T+str(gf)+"/"+str(sf)+"/sampling_time_points_seed_0.npy")
    time_points = [i for i in time_points]
    i=0
    N_lesion = 1000
    str_ll = np.load(T+str(gf)+"/"+str(sf)+"/str_ll_seed_"+str(i)+".npy")
    summ = trapz(time_points[-35::],str_ll[-35::])

    return summ

diff = np.zeros([10,10])
for gf in np.arange(1,11,1):
    for sf in np.arange(1,11,1):
        temp = get_strc_diff(gf,sf)
        diff[sf-1,gf-1] = temp

fig = plt.figure(figsize=(cm2inch(3.), cm2inch(3.)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.9,bottom=0.1,left=0.1,right=0.9,hspace=0.05,wspace=0.05)
ax1 = plt.subplot(gs1[0,0])
cmap='coolwarm'
img=ax1.pcolor(diff.T,cmap=cmap)
ax1.set_ylabel(r"$\nu$")
ax1.set_xlabel(r"$\rho$")
cax = fig.add_axes([0.92,0.1,0.02,0.8])
cbar = plt.colorbar(img,cax=cax,orientation='vertical')
#cbar.set_ticks((np.arange(vmin,vmax+0.01,500000)))
cbar.set_label(r"$\sum \Delta \Gamma_{\mathrm{struc.(S-S)}}$")
cax.yaxis.set_label_position('right')

ax1.set_yticks(np.arange(0,11,2))
ax1.set_yticklabels(["0","20%","40%","60%","80%","100%"])
ax1.set_xticks(np.arange(0,11,2))
ax1.set_xticklabels(np.arange(0,0.11,0.02))
plt.savefig("summary.svg")
plt.show()