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

def plot_matrix(matrix,vmin,vmax,type):
	fig = plt.figure(figsize=(cm2inch(3.), cm2inch(3)))
	gs1 = gridspec.GridSpec(1, 1)
	gs1.update(top=0.9,bottom=0.1,left=0.1,right=0.9,hspace=0.15,wspace=0.15)
	ax1 = plt.subplot(gs1[0,0])

	cmap='Greens'
	averagesize=20

	matrix_reduced = equalize(matrix)
	img = ax1.imshow(matrix_reduced.T,vmin=vmin,vmax=vmax,cmap=cmap,aspect=1.)

	ax1.set_xticks([10,110])
	ax1.set_xticklabels(["S","E"])
	ax1.set_yticks([10,110])
	ax1.set_yticklabels(["S","E"])


	cax = fig.add_axes([0.95,0.1,0.02,0.8])
	cbar = plt.colorbar(img,cax=cax,orientation='vertical')
	if type=="str":
		cbar.set_ticks([0.,0.06,0.12])
		cbar.set_ticklabels(["0%","6%","12%"])
		cbar.set_label(r'$\Gamma_{\mathrm{struc.}}$')

	if type=="eff":
		cbar.set_label(r'$\Gamma_{\mathrm{effec.}}$')
		cbar.set_ticks([0.,0.1,0.2,0.3])
		cbar.set_ticklabels(["0%","10%","20%","30%"])

	cax.yaxis.set_label_position('right')

	



T = "./doubled_SS/"
seed = 0
i = 0

matrix_n = np.load(T+"connectivity_matrix_6900.npy")
matrix_w = np.load(T+"connectivity_matrix_w_6900.npy")
plot_matrix(matrix_n,0.0,0.12,"str")
plt.savefig("conn_matrix_n.svg")

plot_matrix(matrix_w,0.0,0.3,"eff")
plt.savefig("conn_matrix_w.svg")


plt.show()


