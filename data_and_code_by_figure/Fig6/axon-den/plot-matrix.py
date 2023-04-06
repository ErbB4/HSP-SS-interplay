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

fig = plt.figure(figsize=(cm2inch(6), cm2inch(2.7)))
############## plot linear case ###############
gs1 = gridspec.GridSpec(1, 2)
gs1.update(top=0.95,bottom=0.2,left=0.1,right=0.9,hspace=0.01,wspace=0.01)
ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])


cmap='YlOrRd'
averagesize=20

vmin = 0.04
vmax = 0.10

T = "C://Users/han/Desktop/Lab/GaussianHSP-SC/large-network-bg-10s-axon-eta-den-2rules-5seeds/"
seed = 2
matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
matrix_reduced = equalize(matrix)
#img = ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax,aspect=1.)
img = ax1.imshow(matrix_reduced,vmin=vmin,vmax=vmax,cmap=cmap,aspect=1.)

ax1.set_xticks([10,110])
ax1.set_xticklabels(["S","E"])
ax1.set_yticks([10,110])
ax1.set_yticklabels(["S","E"])

seed = 4
matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
matrix_reduced2 = equalize(matrix)
img2 = ax2.imshow(matrix_reduced2,vmin=vmin,vmax=vmax,cmap=cmap,aspect=1.)
#img2 = ax2.imshow(matrix_reduced2,vmin=vmin,vmax=vmax,aspect=1.)

ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_aspect(1)
cax = fig.add_axes([0.95,0.2,0.02,0.75])
cbar = plt.colorbar(img2,cax=cax,orientation='vertical')
cbar.set_ticks([0.04,0.07,0.10])
cbar.set_ticklabels([r"$4\%$",r"$7\%$",r"$10\%$"])
cbar.set_label(r"$\Gamma$")
cax.xaxis.set_label_position('top')
cax.xaxis.set_ticks_position('top')

plt.savefig("conn_matrix.svg")

plt.show()
