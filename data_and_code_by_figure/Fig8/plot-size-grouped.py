import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.gridspec as gridspec
import pingouin as pg 
from scipy import stats
import seaborn as sns

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
    return value/2.54


T = "./data/"
data_raw = pd.read_csv(T+"spine_size_merged.csv")
data = data_raw.copy()


def plot_diffs_histogram_by_size(data,ax,groupname):
    groupdata = data[data["group"]==groupname]
    pre  = groupdata[groupdata["stage"]=="d0"]
    post = groupdata[groupdata["stage"]=="d3"]
    diffs = post["RawIntDen"].values - pre["RawIntDen"].values
    diffs_normed = diffs/pre["RawIntDen"].values

    new_data = pre.loc[:,["Label","RawIntDen","batch","group","stage","culture"]]
    new_data["size_diff"] = diffs
    new_data["size_diff_normed"] = diffs_normed

    counts,lefts = np.histogram(new_data["RawIntDen"].values,bins=8,range=(0,40000))
    sorted_data = new_data.sort_values(by="RawIntDen")

    means = []
    sems = []

    idx_manager = 0
    for i in counts:
        diffs_list = sorted_data["size_diff_normed"].values 
        means.append(np.mean(diffs_list[idx_manager:idx_manager+i]))
        sems.append(sp.stats.sem(diffs_list[idx_manager:idx_manager+i]))
        idx_manager += i
    means = np.array(means)
    sems  = np.array(sems)

    print(groupname)
    print(lefts)
    print(means)

    if groupname == "sham":
        ax.errorbar(lefts[1::],means,yerr=sems,color='#293241',capsize=3.,label='control')

    if groupname == "200nano":
        ax.errorbar(lefts[1::],means,yerr=sems,color='#ee6c4d',capsize=3.,label=r'$200\,\mathrm{nM}$ NBQX')

    if groupname == "50micron":
        ax.errorbar(lefts[1::],means,yerr=sems,color='#98c1d9',capsize=3.,label=r'$50\,\mathrm{\mu M}$ NBQX')

    ax.set_xticks(lefts[1::2])
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    ax.axhline(y=0,linestyle='--',color='grey',linewidth=0.5)
    ax.legend(loc="best",frameon=False)


fig = plt.figure(figsize=(cm2inch(5), cm2inch(3.9)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.99,bottom=0.2,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

plot_diffs_histogram_by_size(data,ax1,"sham")
plot_diffs_histogram_by_size(data,ax1,"200nano")
plot_diffs_histogram_by_size(data,ax1,"50micron")

ax1.set_ylabel(r"$\Delta$ spine size (normalized)")
ax1.set_xlabel("Baseline spine size (a.u.)")

plt.savefig("spine_size-grouped.svg")
plt.show()