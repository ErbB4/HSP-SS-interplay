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
plt.rcParams["lines.linewidth"]=.2
plt.rcParams["lines.markersize"]=5
plt.rcParams["xtick.labelsize"]=6
plt.rcParams["ytick.labelsize"]=6
plt.rcParams["font.family"] = "arial"
plt.rcParams['mathtext.fontset'] = 'dejavusans'
plt.rcParams["legend.fontsize"] = 6

def cm2inch(value):
    #transfer the unit of figure size from cm to inch
    return value/2.54

def plot_rast(times, senders,sampling_time_point):
    fig = plt.figure(figsize=(cm2inch(1.5), cm2inch(4.)))
    gs1 = gridspec.GridSpec(1, 1)
    gs1.update(top=0.99,bottom=0.05,left=0.01,right=0.99,hspace=0.2,wspace=0.3)
    ax1 = plt.subplot(gs1[0,0]) #plot raster plot for a few neurons

    senders_temp_1 = senders[np.where(senders<1101)]
    times_temp_1   = times[np.where(senders<1101)]

    senders_non_dep = senders_temp_1[np.where(senders_temp_1>1000)]
    times_non_dep   = times_temp_1[np.where(senders_temp_1>1000)]

    senders_temp_2 = senders[np.where(senders<1000)]
    time_temp_2    = times[np.where(senders<1000)]

    senders_dep = senders_temp_2[np.where(senders_temp_2>899)]
    times_dep   = time_temp_2[np.where(senders_temp_2>899)]

    senders_temp_3 = senders[np.where(senders>10000)]
    time_temp_3    = times[np.where(senders>10000)]

    senders_inh = senders_temp_3[np.where(senders_temp_3<10101)]
    times_inh   = time_temp_3[np.where(senders_temp_3<10101)]

    ax1.plot(times_non_dep/1000.,senders_non_dep,'|',markersize=1.5,color='#47abd8')
    ax1.plot(times_dep/1000.,senders_dep,'|',markersize=1.5,color='#666666')
    ax1.plot(times_inh/1000.,senders_inh-8900,'|',markersize=1.5,color='#d01b1b')
    ax1.set_xlim(sampling_time_point/1000.-1,sampling_time_point/1000.-0.8)

    ax1.spines['right'].set_visible(False)
    ax1.spines['left'].set_visible(False)
    ax1.spines['top'].set_visible(False)
    ax1.spines['bottom'].set_visible(False)

    ax1.yaxis.set_ticks_position('left')
    ax1.xaxis.set_ticks_position('bottom')
    ax1.set_xticks([])
    ax1.set_yticks([])
    if sampling_time_point == 6900000.0:
        pass


################# get data for three time points ############
T = "./doubled_SS/raster_data/"
sampling_time_points = np.load(T+"sampling_time_points_seed_0.npy")

for sampling_time_point in [6000000.0,6900000.0,7500000.0]:
    times   = np.load(T+"times_"+str(sampling_time_point)+".npy")
    senders = np.load(T+"senders_"+str(sampling_time_point)+".npy")

    plot_rast(times, senders,sampling_time_point)
    plt.savefig(str(sampling_time_point)+".svg")

plt.show()