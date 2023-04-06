import numpy as np
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.gridspec as gridspec



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

fig = plt.figure(figsize=(cm2inch(11), cm2inch(3.)))
gs1 = gridspec.GridSpec(1, 3)
gs1.update(top=0.9,bottom=0.2,left=0.12,right=0.95,hspace=0.05,wspace=0.15)

ax1 = plt.subplot(gs1[0,0])
ax2 = plt.subplot(gs1[0,1])
ax3 = plt.subplot(gs1[0,2])



eps   = 0.0079
eta_1 = 0.
eta_2 = 0.0007

slope = 0.5
x = np.arange(0,0.016,0.00001)



for factor in [1.0,0.5,0.1]:
    
    #linear rule
	y_linear = factor * x * (-1 * slope) + eps * slope * factor
	ax1.plot(x*1000,10*y_linear,'-',color='#343a40ff',alpha=factor,label="{:.0%}".format(factor))

	#gaussian_rule, eta=0.0
	nv   = slope * factor * eps
	xi   = (eta_1 + eps)/2.
	zeta = (eta_1-eps)/(2.*np.sqrt(-1*(np.log(1/2))))

	y_gaussian_1 = nv * (2*np.exp(-1*((x-xi)/zeta)**2)-1)
	ax2.plot(x*1000,10*y_gaussian_1,'-',color='#343a40ff',alpha=factor)

	#gaussian_rule,eta=0.002
	nv   = slope * factor * eps
	xi   = (eta_2 + eps)/2.
	zeta = (eta_2-eps)/(2.*np.sqrt(-1*(np.log(1/2))))

	y_gaussian_1 = nv * (2*np.exp(-1*((x-xi)/zeta)**2)-1)
	ax3.plot(x*1000.,10*y_gaussian_1,'-',color='#343a40ff',alpha=factor)


for ax in [ax1,ax2,ax3]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	ax.ticklabel_format(axis='y',style='sci')
	ax.axhline(y=0,color='gray',linestyle='--',linewidth=0.5)
	ax.axvline(x=7.9,color='#ee6c4d',linestyle='--',linewidth=0.5)
	ax.set_xticks(np.arange(0,17,2))
	ax.set_ylim(-0.05,0.05)


ax1.legend(loc='upper right',frameon=False)
ax1.set_ylabel("Elements per update")
ax1.set_title("$\it{Linear}$")
ax1.set_yticks([-0.025,0.025])


ax2.set_xlabel("Activity (Hz)")
ax2.axvline(x=7.9,color='#ee6c4d',linestyle='--',linewidth=0.5)
ax2.axvline(x=0,color='gray',linestyle='--',linewidth=0.5)
ax2.set_yticks([])
ax2.set_title("$\it{Gaussian\ (\eta=0)}$")

ax3.set_yticks([])
ax3.axvline(x=0.7,color='gray',linestyle='--',linewidth=0.5)
ax3.set_title("$\it{Gaussian\ (\eta>0)}$")

plt.savefig("growth_rule.svg")
plt.show()

