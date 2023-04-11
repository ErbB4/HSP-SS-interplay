import numpy as np 
import scipy as sp 
import matplotlib.pyplot as plt 
import pandas as pd 
import matplotlib.gridspec as gridspec
import pingouin as pg 
from scipy import stats
import seaborn as sns 
from scipy.stats import pearsonr


def reorganize_data(data):
    pre  = data[data["stage"]=="d0"]
    post = data[data["stage"]=="d3"]
    new_data = pre.loc[:,["Label","RawIntDen","batch","group","segment_ID"]]
    new_data["post_RawIntDen"] = post["RawIntDen"].values
    new_data.rename(columns={'RawIntDen':'pre_RawIntDen'}, inplace=True)
    return new_data

def get_spine_density_change(datadensity,segment_ID):
    subdata = datadensity[datadensity["segment_ID"]==segment_ID]
    diffs   = subdata[subdata["stage"]=="after"]["spine_density"].values - subdata[subdata["stage"]=="before"]["spine_density"].values
    return diffs

def get_average_spine_size_change(datasize,segment_ID):
    subdata = datasize[datasize["segment_ID"]==segment_ID]
    diffs   = subdata["post_RawIntDen"].values - subdata["pre_RawIntDen"].values
    return np.mean(diffs),sp.stats.sem(diffs)

def annotate_density_in_target_files(datasize,datadensity):
    for name in np.unique(datadensity["segment_ID"]):
        diffs_size = get_average_spine_size_change(datasize,name)
        diffs_density = get_spine_density_change(datadensity,name)
        datadensity.loc[datadensity["segment_ID"]==name,"spine_size_diff"]     = diffs_size[0]
        datadensity.loc[datadensity["segment_ID"]==name,"spine_size_diff_sem"] = diffs_size[1]
        datadensity.loc[datadensity["segment_ID"]==name,"spine_density_diff"]  = diffs_density[0]
        datadensity.loc[datadensity["segment_ID"]==name,"spine_density_diff_abs"]  = abs(diffs_density[0])
    return datadensity

def plot_fit_curves(data,groupname,direction,ax,palette):
    subdata = data[data["group"]==groupname]
    print(groupname)
    print(direction)
    print(len(subdata))
    theta = np.polyfit(subdata["spine_density"].values, subdata["spine_size_diff"].values, 1)
    cov = pearsonr(subdata["spine_density"].values,subdata["spine_size_diff"].values)
    print(cov)
    if cov[1]>0.05:
        pass
    else: 
        x = np.arange(0.5,3.0,0.1)
        if groupname=="sham":
            color = palette[0]
        if groupname=="200nano":
            color = palette[1]
        if groupname=="50micro":
            color = palette[2]

        if direction=="increased":
            ax.plot(x,theta[1]+theta[0]*x,'-',color=color)
        if direction=="decreased":
            ax.plot(x,theta[1]+theta[0]*x,'--',color=color)
        if direction=="all":
            ax.plot(x,theta[1]+theta[0]*x,'-',color=color)


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

T = "./"
data_raw = pd.read_csv(T+"spine_size_merged.csv")
size_raw = data_raw.copy()
size_raw["segment_ID"] = size_raw["batch"].astype(str) + "-" + size_raw["culture"].astype(str)
size = reorganize_data(size_raw)

T = "./"
data_raw = pd.read_csv(T+"data_density_merged.csv")
density = data_raw.copy()

data_all = annotate_density_in_target_files(size,density)
data_half = data_all[data_all["stage"]=="before"]

fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(4.5)))
gs = gridspec.GridSpec(1, 1)
gs.update(top=0.9,bottom=0.23,left=0.23,right=0.9,hspace=0.1,wspace=0.15)
ax = plt.subplot(gs[0,0])

fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(4.5)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.9,bottom=0.23,left=0.23,right=0.9,hspace=0.1,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])

fig = plt.figure(figsize=(cm2inch(4.5), cm2inch(4.5)))
gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.9,bottom=0.23,left=0.23,right=0.9,hspace=0.1,wspace=0.15)
ax2 = plt.subplot(gs1[0,0])


data_increased = data_half[data_half["spine_density_diff"]>0]
data_decreased = data_half[data_half["spine_density_diff"]<0]

palette = ['#293241','#ee6c4d','#98c1d9']
sns.scatterplot(data=data_half,x="spine_density",y="spine_size_diff",size="spine_density_diff",sizes=(5,50),size_order=[0.2,0.4,0.6,0.8,1.0],hue="group",hue_order=["sham","200nano","50micro"],palette=palette,ax=ax)
sns.scatterplot(data=data_increased,x="spine_density",y="spine_size_diff",size="spine_density_diff",sizes=(5,50),size_order=[0.2,0.4,0.6,0.8,1.0],hue="group",hue_order=["sham","200nano","50micro"],palette=palette,ax=ax1)
sns.scatterplot(data=data_decreased,x="spine_density",y="spine_size_diff",size="spine_density_diff_abs",sizes=(5,50),size_order=[0.2,0.4,0.6,0.8,1.],hue="group",hue_order=["sham","200nano","50micro"],palette=palette,ax=ax2)#,marker="x")

#fit curves
plot_fit_curves(data_half,"sham","all",ax,palette)
plot_fit_curves(data_increased,"sham","increased",ax1,palette)
plot_fit_curves(data_decreased,"sham","decreased",ax2,palette)

plot_fit_curves(data_half,"200nano","all",ax,palette)
plot_fit_curves(data_increased,"200nano","increased",ax1,palette)
plot_fit_curves(data_decreased,"200nano","decreased",ax2,palette)

plot_fit_curves(data_half,"50micro","all",ax,palette)
plot_fit_curves(data_increased,"50micro","increased",ax1,palette)
plot_fit_curves(data_decreased,"50micro","decreased",ax2,palette)


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.yaxis.set_ticks_position('left')
ax1.xaxis.set_ticks_position('bottom')

ax2.spines['right'].set_visible(False)
ax2.spines['top'].set_visible(False)
ax2.yaxis.set_ticks_position('left')
ax2.xaxis.set_ticks_position('bottom')

ax.set_xlabel(r"Baseline spine density (per $\mu$m)")
ax.set_ylabel(r"$\bar{\Delta}$ spine size (a.u.)")
ax.axhline(y=0,linestyle='--',color='grey',linewidth=0.5)
ax.text(1.8,5400,r'$r(24)=0.65$',fontsize=8)

ax1.set_xlabel(r"Baseline spine density (per $\mu$m)")
ax1.set_ylabel(r"$\bar{\Delta}$ spine size (a.u.)")
ax1.axhline(y=0,linestyle='--',color='grey',linewidth=0.5)

ax2.set_xlabel(r"Baseline spine density (per $\mu$m)")
ax2.set_ylabel(r"$\bar{\Delta}$ spine size (a.u.)")
ax2.axhline(y=0,linestyle='--',color='grey',linewidth=0.5)

ax.get_legend().remove()
ax1.get_legend().remove()
ax2.get_legend().remove()

ax.set_xlim(0.5,3.0)
ax1.set_xlim(0.5,3.0)
ax2.set_xlim(0.5,3.0)

ax.set_ylim(-6500,6500)
ax1.set_ylim(-6500,6500)
ax2.set_ylim(-6500,6500)

ax1.set_title("Segments w/ increased\nspine density")
ax2.set_title("Segments w/ reduced\nspine density")

plt.figure(1)
plt.savefig("size_and_density_all.svg")

plt.figure(2)
plt.savefig("size_and_density_increased.svg")

plt.figure(3)
plt.savefig("size_and_density_decrease.svg")
plt.show()
