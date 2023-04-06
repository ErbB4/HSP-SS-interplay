import numpy as np
import matplotlib.pyplot as plt
from parameters import *
from matplotlib import gridspec

#####get data and downsize matrix#####

def equalize(matrix,size=50):
    matrix_reduced = np.zeros((int(NE/size),int(NE/size)))
    for i in np.arange(0,int(NE/size),1):
        for j in np.arange(0,int(NE/size),1):
            matrix_reduced[i,j] = np.mean(matrix[i*size:(i+1)*size,j*size:(j+1)*size])
    return matrix_reduced


NE = 10000


####setting for figures####
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=2.
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



fig = plt.figure(figsize=(cm2inch(3.2), cm2inch(2.8)))

############## plot linear case ###############

gs1 = gridspec.GridSpec(1, 1)
gs1.update(top=0.95,bottom=0.05,left=0.15,right=0.85,hspace=0.05,wspace=0.15)
ax1 = plt.subplot(gs1[0,0])


cmap='plasma'
averagesize=20

vmin = 0.0
vmax = 0.06


T = "./"
seed = 0
i = 0

matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")

matrix_reduced = equalize(matrix)
img = ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax,cmap=cmap,aspect='auto')
ax1.set_xticks([0,100,200])
ax1.set_xticklabels([0,5000,10000])
ax1.set_yticks([0,100,200])
ax1.set_yticklabels([0,5000,10000])

ax1.set_xlabel("Presynaptic neuron")
ax1.set_ylabel("Postsynaptic neuron")

cax = fig.add_axes([0.87,0.05,0.02,0.9])
cbar = plt.colorbar(img,cax=cax,orientation='vertical')
cbar.set_ticks([0,0.03,0.06])
cbar.set_ticklabels(["0%","3%","6%"])
cbar.set_label(r"$\Gamma$")
cax.yaxis.set_label_position('right')


plt.savefig("conn_matrix.svg")

plt.show()
