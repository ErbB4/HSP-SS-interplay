import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.gridspec as gridspec
import pingouin as pg 
from scipy import stats
import seaborn as sns 


####figure settings####
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
    return value/2.54

T = "./data/"
data = pd.read_csv(T+"ephys_data.csv")

def plot_scatter(data,ax,parameter):
    sns.boxplot(data=data,x="group",y=parameter,order=["control","200nano","50micron"],color='w',showfliers = False,saturation=1.,ax=ax)
    plt.setp(ax.artists, edgecolor = 'k', facecolor='w')
    plt.setp(ax.lines, color='k')
    sns.swarmplot(data=data,x="group", y=parameter, size=4.,order=["control","200nano","50micron"],palette=["#293241","#ee6c4d","#98c1d9"],ax=ax)


fig = plt.figure(figsize=(cm2inch(5), cm2inch(3.09)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.95,bottom=0.25,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])

fig = plt.figure(figsize=(cm2inch(5), cm2inch(3.09)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.95,bottom=0.25,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax2 = plt.subplot(gs1[0,0])

plot_scatter(data,ax1,"frequency")
plot_scatter(data,ax2,"amplitude")

for ax in [ax1,ax2]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xticklabels(["control",r"$200\,\mathrm{nM}$", r"$50\,\mathrm{\mu M}$"])
    ax.set_xlabel("NBQX concentration")

ax1.set_ylabel("sEPSC frequency (Hz)")
ax2.set_ylabel("sEPSC amplitude (pA)")


# for a unified data storage and documentation, statistics was perfromed in Prisma and documented in the lab
ax1.text(1,2.2,"*",fontsize=10,va="bottom",ha="center")
ax1.text(2,0.8,"***",fontsize=10,va="bottom",ha="center")

ax2.text(1,32,"ns",fontsize=8,va="bottom",ha="center")
ax2.text(2,25,"***",fontsize=10,va="bottom",ha="center")

plt.figure(1)
plt.savefig("ephys_freq.png")
plt.figure(2)
plt.savefig("ephys_amp.svg")


plt.show()