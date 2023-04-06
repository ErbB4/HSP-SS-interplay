import numpy as np
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.gridspec as gridspec
import pandas as pd 
import seaborn as sns
import scipy as sp 
from scipy import stats 


T = "./data/"
data_raw = pd.read_csv(T+"spine_size_merged.csv")
data = data_raw.copy()

def get_subdata(data,groupname):
    subdata = data[data["group"]==groupname]
    return subdata

def plot_lines(data,ax,groupname,normed=True):
    subdata = get_subdata(data,groupname)
    before  = subdata[subdata["stage"]=="d0"]["RawIntDen"].values
    after   = subdata[subdata["stage"]=="d3"]["RawIntDen"].values
    ratio = after/before

    if groupname == "sham":
        color = "#293241"
    if groupname == "200nano":
        color = "#ee6c4d"
    if groupname == "50micron":
        color = "#98c1d9"

    if normed == False:
        ax.errorbar(x=[0,1],y=[np.mean(before),np.mean(after)],yerr=[sp.stats.sem(before),sp.stats.sem(after)],linewidth=1.5,color=color,ecolor=color)

    if normed == True:
        if groupname == "sham":
            ax.errorbar(x=[0,1],y=[1,np.mean(ratio)],yerr=[0,sp.stats.sem(ratio)],linewidth=1.5,color=color,ecolor=color,label="control")

        if groupname == "200nano":
            ax.errorbar(x=[0,1],y=[1,np.mean(ratio)],yerr=[0,sp.stats.sem(ratio)],linewidth=1.5,color=color,ecolor=color,label=r"$200\,\mathrm{nM}$ NBQX")

        if groupname == "50micron":
            ax.errorbar(x=[0,1],y=[1,np.mean(ratio)],yerr=[0,sp.stats.sem(ratio)],linewidth=1.5,color=color,ecolor=color,label=r"$50\,\mathrm{\mu M}$ NBQX")




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

fig = plt.figure(figsize=(cm2inch(1.5), cm2inch(1.5)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.95,bottom=0.05,left=0.05,right=0.95,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])

plot_lines(data,ax1,"sham")
plot_lines(data,ax1,"200nano")
plot_lines(data,ax1,"50micron")


for ax in [ax1]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

ax1.set_ylabel("Normalized\nspine size")
ax1.ticklabel_format(axis='y',style='sci')
ax1.set_xlim(-0.1,1.1)
ax1.set_ylim(0.9,1.65)
ax1.set_yticks([1.,1.5])
ax1.set_xticks([0,1])
ax1.set_xticklabels(["baseline","after"])

plt.savefig("spine_size_inset.svg")
plt.show()

