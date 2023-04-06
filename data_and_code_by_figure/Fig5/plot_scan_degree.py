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

############## load data #####################
fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(3.8)))

############## plot linear case ###############
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.97,bottom=0.22,left=0.15,right=0.95,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0:2,0])

def get_conn_sum(T,n):
    conn_sum = []
    for seed in np.arange(0,n,1):
        connectivity_ss = np.load(T+"connectivity_ss_seed_"+str(seed)+".npy")
        conn_sum.append(np.sum(connectivity_ss[19::]))
    return conn_sum

def get_conn_last(T,n):
    conn_last = []
    print(T)
    for seed in np.arange(0,n,1):
        connectivity_ss = np.load(T+"connectivity_ss_seed_"+str(seed)+".npy")
        conn_last.append(connectivity_ss[-1])

        print(connectivity_ss[-1])
    return conn_last


degree_linear_mean = np.load("linear_mean_degree.npy")
degree_linear_std = np.load("linear_std_degree.npy")

degree_gaussian_mean = np.load("gaussian_mean_degree.npy")
degree_gaussian_std = np.load("gaussian_std_degree.npy")

degree_eta_mean = np.load("eta_mean_degree.npy")
degree_eta_std = np.load("eta_std_degree.npy")

x1 = np.array([0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.95,1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,2.0])
ax1.plot(x1[4:14],degree_linear_mean[4:14],".-",color='#606c38',label='Linear')
ax1.plot(x1[0:4],degree_linear_mean[0:4],"o",markeredgecolor='#606c38',markerfacecolor='none')
ax1.plot(x1[14::],degree_linear_mean[14::],"o",markeredgecolor='#606c38',markerfacecolor='none')

ax1.fill_between(x1[4:14],degree_linear_mean[4:14]-degree_linear_std[4:14],degree_linear_mean[4:14]+degree_linear_std[4:14],color='#606c38',alpha=0.2)

ax1.plot(x1,degree_eta_mean,"|-",markersize=7,color='#dda15e',label='Gaussian '+r'$(\eta=0)$')
ax1.fill_between(x1,degree_eta_mean-degree_eta_std,degree_eta_mean+degree_eta_std,color='#dda15e',alpha=0.2)       

ax1.plot(x1,degree_gaussian_mean,".-",markersize=2,color='#bc6c25',label='Gaussian '+r'$(\eta>0)$')       
ax1.fill_between(x1,degree_gaussian_mean-degree_gaussian_std,degree_gaussian_mean+degree_gaussian_std,color='#bc6c25',alpha=0.2)       

ax1.legend(loc='best',frameon=False)
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')
ax1.axvline(x=1.,color='gray',linestyle='--',linewidth=0.5)

ax1.set_xlabel("FOI")
ax1.set_xticks([0,0.5,1.,1.5,2.])
ax1.set_xticklabels([r'$0\%$',r'$50\%$',r'$100\%$',r'$150\%$',r'$200\%$'])
ax1.set_ylabel(r"$\#\ \mathrm{incoming\ synapses}$")

plt.savefig("scan_degree.svg")
plt.show()
        
