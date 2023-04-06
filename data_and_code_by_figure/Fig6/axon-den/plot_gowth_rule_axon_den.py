import numpy as np
import matplotlib.pyplot as plt 
import numpy as np 
import matplotlib.gridspec as gridspec



#define plotting parameters
plt.rcParams["axes.titlesize"]=10
plt.rcParams["axes.labelsize"]=8
plt.rcParams["axes.linewidth"]=.5
plt.rcParams["lines.linewidth"]=1.
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

fig = plt.figure(figsize=(cm2inch(3.5), cm2inch(2.5)))
gs1 = gridspec.GridSpec(2, 2)
gs1.update(top=0.9,bottom=0.05,left=0.05,right=0.95,hspace=0.4,wspace=0.4)

ax1 = plt.subplot(gs1[1,0])
ax2 = plt.subplot(gs1[1,1])
ax3 = plt.subplot(gs1[0,1])


def get_gaussian_curve(x,eta):
	eps   = 0.0079
	slope = 0.5
	factor=0.1
	nv   = slope * factor * eps
	xi   = (eta + eps)/2.
	zeta = (eta-eps)/(2.*np.sqrt(-1*(np.log(1/2))))
	y_gaussian = nv * (2*np.exp(-1*((x-xi)/zeta)**2)-1)
	return y_gaussian

x = np.arange(0,0.01,0.00001)

#den<axon
y_gaussian_den_1  = get_gaussian_curve(x,0.001)
y_gaussian_axon_1 = get_gaussian_curve(x,0.003)

ax1.plot(x*1000.,10*y_gaussian_den_1,'-',color='#ccc5b9ff',alpha=1,label='D')
ax1.plot(x*1000.,10*y_gaussian_axon_1,'-',color='#e26d5cff',alpha=1,label='A')


#den>axon
y_gaussian_den_2  = get_gaussian_curve(x,0.003)
y_gaussian_axon_2 = get_gaussian_curve(x,0.001)

ax2.plot(x*1000.,10*y_gaussian_den_2,'-',color='#ccc5b9ff')
ax2.plot(x*1000.,10*y_gaussian_axon_2,'-',color='#e26d5cff')

#den=axon
y_gaussian_den_3  = get_gaussian_curve(x,0.003)
y_gaussian_axon_3 = get_gaussian_curve(x,0.003)

ax3.plot(x*1000.,10*y_gaussian_den_3,'-',color='#ccc5b9ff')
ax3.plot(x*1000.,10*y_gaussian_axon_3,'-',color='#e26d5cff')

for ax in [ax1,ax2,ax3]:
	ax.spines['right'].set_visible(False)
	ax.spines['top'].set_visible(False)
	ax.spines['left'].set_visible(False)
	ax.spines['bottom'].set_visible(False)

	ax.yaxis.set_ticks_position('left')
	ax.xaxis.set_ticks_position('bottom')
	ax.ticklabel_format(axis='y',style='sci')
	ax.set_xticks([])
	ax.set_yticks([])
	ax.set_xlim((-0.1,10))

	ax.axhline(y=0,color='gray',linestyle='--',linewidth=0.5)



ax1.legend(bbox_to_anchor=(0., 1., 1.8, 0.3), loc=3,ncol=2, mode="expand", borderaxespad=0.,frameon=False)
ax3.text(-1.5,-0.002,"retrac.",fontsize=6.,ha='center',va='center')
ax3.text(-1.5,0.002,"outgr.",fontsize=6.,ha='center',va='center')


plt.savefig("growth_rule.svg")
plt.show()

