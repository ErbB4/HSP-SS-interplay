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


def data_check(data):
    a = 0
    for batch in np.unique(data["batch"]):
        subdata = data[data["batch"]==batch]
        for culture in np.unique(subdata["culture"]):
            segdata = subdata[subdata["culture"]==culture]
            if len(segdata) %2 !=0:
                print("culture not matched:"+str(culture))
                print(str(batch))
                a = a+1
            else:
                pass
    if a==0:
        print("all culture pairs are matched!")


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
            pre  = np.hstack([pre,d0_value])
            post = np.hstack([post,d3_value])
    return pre,post

def get_subdata(data,groupname):
    groupdata = data[data["group"]==groupname]
    pre,post = get_pre_post(groupdata)
    return pre,post

def get_difference(data,groupname):
    pre,post = get_subdata(data,groupname)
    diffs = post-pre
    return diffs

def get_cdf(data_list):
    x = np.sort(data_list)
    y = 1.*np.arange(0,len(data_list),1.)/ (len(data_list)-1)
    return x,y

def plot_diffs_histogram(data,ax,groupname):
    pre,post  = get_subdata(data,groupname)
    diffs     = get_difference(data,groupname)
    diffs_norm = diffs/pre
    if groupname == "sham":
       ax.plot(get_cdf(pre)[0],get_cdf(pre)[1],color='#293241',linestyle=':',label='baseline')
       ax.plot(get_cdf(post)[0],get_cdf(post)[1],color='#293241',linestyle='-',label='control')
       ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
       ax.legend(bbox_to_anchor=(0.00, 0.85, 1.1, 0.3), loc=1,ncol=2, mode="expand", borderaxespad=0.,frameon=False)

    if groupname == "200nano":
       ax.plot(get_cdf(pre)[0],get_cdf(pre)[1],color='#293241',linestyle=':')
       ax.plot(get_cdf(post)[0],get_cdf(post)[1],color='#ee6c4d',linestyle='-',label=r'$200\,\mathrm{nM}$ NBQX')
       ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
       ax.legend(bbox_to_anchor=(0.00, 0.85, 0.98, 0.3), loc=1,ncol=2, mode="expand", borderaxespad=0.,frameon=False)

    if groupname == "50micron":
       ax.plot(get_cdf(pre)[0],get_cdf(pre)[1],color='#293241',linestyle=':')
       ax.plot(get_cdf(post)[0],get_cdf(post)[1],color='#98c1d9',linestyle='-',label=r'$50\,\mathrm{\mu M}$ NBQX')
       ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
       ax.legend(bbox_to_anchor=(0.00, 0.85, 0.98, 0.3), loc=1,ncol=2, mode="expand", borderaxespad=0.,frameon=False,fontsize=6)

    
#check if each spine has its pre and post measurements.
data_check(data)    

fig = plt.figure(figsize=(cm2inch(10), cm2inch(3.9)))
gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.9,bottom=0.22,left=0.1,right=0.99,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])
ax1.set_ylabel("cdf")
ax2.set_xlabel("Spine size (a.u)")

# for a unified data storage and documentation, statistics was perfromed in Prisma and documented in the lab
ax1.text(9900,0.95,"ns",fontsize=8,va="center",ha="center")
ax2.text(9900,0.95,"***",fontsize=10,va="center",ha="center")
ax3.text(9900,0.95,"***",fontsize=10,va="center",ha="center")


plot_diffs_histogram(data,ax1,"sham")
plot_diffs_histogram(data,ax2,"200nano")
plot_diffs_histogram(data,ax3,"50micron")



for ax in [ax1,ax2,ax3]:
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax2.set_yticks([])
    ax3.set_yticks([])

plt.savefig("spine_size.svg")
plt.show()