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
def cm2inch(value):
    return value/2.54


T = "./"
data_raw = pd.read_csv(T+"spine_size_merged.csv")
data = data_raw.copy()



def data_check(subdata):
    for batch in np.unique(data["batch"]):
        subdata = data[data["batch"]==batch]
        for culture in np.unique(subdata["culture"]):
            segdata = subdata[subdata["culture"]==culture]
            if len(segdata) %2 !=0:
                print("culture:"+str(culture))
                print(str(batch))
            else:
                print("culture pairs are matched!")


def get_pre_post(groupdata):
    pre  = np.array([])
    post = np.array([])
    for batch in np.unique(groupdata["batch"]):
        subdata = groupdata[groupdata["batch"]==batch]
        for culture in np.unique(subdata["culture"]):
            segdata = subdata[subdata["culture"]==culture]
            d0 = segdata[segdata["stage"]=="d0"]
            d3 = segdata[segdata["stage"]=="d3"]
            d0_value = np.array(d0["RawIntDen"].values)
            d3_value = np.array(d3["RawIntDen"].values)
            #print(str(culture))
            pre  = np.hstack([pre,d0_value])
            post = np.hstack([post,d3_value])
    return pre,post

def get_subdata(data,groupname):
    groupdata = data[data["group"]==groupname]
    pre,post = get_pre_post(groupdata)
    return pre,post

def get_subdata_normed(data,groupname):
    groupdata = data[data["group"]==groupname]
    pre,post = get_pre_post(groupdata)
    normed = post/pre
    normed = [i[0] for i in normed]
    return np.array([1]*len(pre)),normed

def get_difference(data,groupname):
    pre,post = get_subdata(data,groupname)
    diffs = post-pre
    return diffs




def plot_initial_size_histogram(data,ax,groupname):
    pre,post  = get_subdata(data,groupname)

    if groupname == "sham":
       ax.hist(pre,histtype="bar",color='#293241',linestyle='--',bins=50,label='control')

    if groupname == "200nano":
       ax.hist(pre,histtype="bar",color='#ee6c4d',linestyle='--',bins=50,label=r"$200\,\mathrm{nM}$ NBQX")

    if groupname == "50micron":
       ax.hist(pre,histtype="bar",color='#98c1d9',linestyle='--',bins=50,label=r"$50\,\mathrm{\mu M}$ NBQX")

    ax.legend(bbox_to_anchor=(0.05, 0.85, 0.95, 0.3), loc=1,ncol=2, mode="expand", borderaxespad=0.,frameon=False,fontsize=6)
    ax.set_ylabel(r"$\#$ spines")
    ax.legend(loc='upper right',frameon=False)


def plot_initial_size_histogram_density(data,ax,groupname):
    pre,post  = get_subdata(data,groupname)

    if groupname == "sham":
        ax.hist(pre,histtype="step",color='#293241',linestyle='-',bins=50,density=True,label='control')

    if groupname == "200nano":
        ax.hist(pre,histtype="step",color='#ee6c4d',linestyle='-',bins=50,density=True,label=r"$200\,\mathrm{nM}$ NBQX")

    if groupname == "50micron":
        ax.hist(pre,histtype="step",color='#98c1d9',linestyle='-',bins=50,density=True,label=r"$50\,\mathrm{\mu M}$ NBQX")

    ax.legend(bbox_to_anchor=(0.45, 0.55, 0.5, 0.3), loc=1,ncol=1, mode="expand", borderaxespad=0.,frameon=False,fontsize=6)


def plot_diffs_histogram_by_size(data,ax,groupname):
    groupdata = data[data["group"]==groupname]
    pre  = groupdata[groupdata["stage"]=="d0"]
    post = groupdata[groupdata["stage"]=="d3"]
    diffs = post["RawIntDen"].values - pre["RawIntDen"].values
    diffs_normed = diffs/pre["RawIntDen"].values
    #diffs_normed = post["RawIntDen"].values/pre["RawIntDen"].values

    new_data = pre.loc[:,["Label","RawIntDen","batch","group","stage","culture"]]
    new_data["size_diff"] = diffs
    new_data["size_diff_normed"] = diffs_normed

    counts,lefts = np.histogram(new_data["RawIntDen"].values,bins=8,range=(0,40000))
    sorted_data = new_data.sort_values(by="RawIntDen")

    means = []
    sems = []

    idx_manager = 0
    for i in counts:
        #diffs_list = sorted_data["size_diff"].values 

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
       #,color='#293241',label='sham')
       #ax.hist(post,histtype="step",color='#293241',linestyle='-',bins=50,cumulative=True,density=True,label='sham')
       #pass

    if groupname == "200nano":
        ax.errorbar(lefts[1::],means,yerr=sems,color='#ee6c4d',capsize=3.,label=r'$200\,\mathrm{nM}$ NBQX')
       #ax.hist(pre,histtype="step",color='#293241',linestyle='--',bins=50,cumulative=True,density=True,label='pre')
       #ax.hist(post,histtype="step",color='#ee6c4d',linestyle='-',bins=50,cumulative=True,density=True,label=r'$200\,\mathrm{nM}$')
       #pass

    if groupname == "50micron":
        ax.errorbar(lefts[1::],means,yerr=sems,color='#98c1d9',capsize=3.,label=r'$50\,\mathrm{\mu M}$ NBQX')
       #ax.hist(pre,histtype="step",color='#293241',linestyle='--',bins=50,cumulative=True,density=True,label='pre')
       #ax.hist(post,histtype="step",color='#98c1d9',linestyle='-',bins=50,cumulative=True,density=True,label=r'$50\,\mathrm{\mu M}$')
       #pass

    #ax.legend(bbox_to_anchor=(0.05, 0.85, 0.95, 0.3), loc=1,ncol=2, mode="expand", borderaxespad=0.,frameon=False,fontsize=6)
    ax.set_xticks(lefts[1::2])
    #ax.set_xticklabels(lefts[1::2])
    ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
    ax.axhline(y=0,linestyle='--',color='grey',linewidth=0.5)
    ax.legend(loc="best",frameon=False)




fig = plt.figure(figsize=(cm2inch(5), cm2inch(4)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.99,bottom=0.2,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])

fig = plt.figure(figsize=(cm2inch(5), cm2inch(4)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.99,bottom=0.2,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax2 = plt.subplot(gs1[0,0])

fig = plt.figure(figsize=(cm2inch(5), cm2inch(4)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.99,bottom=0.2,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax3 = plt.subplot(gs1[0,0])

fig = plt.figure(figsize=(cm2inch(5), cm2inch(4)))
gs1 = gridspec.GridSpec(1,1)
gs1.update(top=0.99,bottom=0.2,left=0.2,right=0.99,hspace=0.05,wspace=0.15)
ax4 = plt.subplot(gs1[0,0])

for ax in [ax1,ax2,ax3,ax4]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.set_xlim(0,40000)
    if ax !=ax4:
        ax.set_ylim(0,80)

    #ax.set_ylabel(r"$\Delta$ spine size (normalized)")
    ax.set_xlabel("Baseline spine size (a.u.)")


plot_initial_size_histogram(data,ax1,"sham")
plot_initial_size_histogram(data,ax2,"200nano")
plot_initial_size_histogram(data,ax3,"50micron")

plot_initial_size_histogram_density(data,ax4,"sham")
plot_initial_size_histogram_density(data,ax4,"200nano")
plot_initial_size_histogram_density(data,ax4,"50micron")


plt.figure(1)
plt.savefig("control.svg")

plt.figure(2)
plt.savefig("200nano.svg")

plt.figure(3)
plt.savefig("50micro.svg")

plt.figure(4)
plt.savefig("density.svg")
plt.show()