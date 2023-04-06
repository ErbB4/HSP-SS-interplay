#This code will get indegree and outdegree from connection matrix.
#It is not necessary to run this code for plotting because the in/out degrees are already stored in the main folder.

import numpy as np

def degree(data):
    indegree = np.sum(matrix,axis=0)
    outdegree = np.sum(matrix,axis=1)
    degree_counts = indegree + outdegree
    return degree_counts

def indegree(data):
    indegree = np.sum(matrix,axis=0)
    return indegree


######################### linear ###################

T = "./linear/"

means = []
stds  = []
for seed in np.arange(0,15,1):
	matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
	degree_counts = indegree(matrix)

	means.append(np.mean(degree_counts[0:1000]))
	stds.append(np.std(degree_counts[0:1000]))

for seed in np.arange(15,22,1):
	means.append(0.)
	stds.append(0.)

np.save("linear_mean_degree.npy",means)
np.save("linear_std_degree.npy",stds)


####################### Gaussian ######################
T = "./Gaussian/"

means = []
stds  = []
for seed in np.arange(0,22,1):
	matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
	degree_counts = indegree(matrix)

	means.append(np.mean(degree_counts[0:1000]))
	stds.append(np.std(degree_counts[0:1000]))


np.save("gaussian_mean_degree.npy",means)
np.save("gaussian_std_degree.npy",stds)


####################### eta ######################
T = "./Gaussian-0eta/"

means = []
stds  = []
for seed in np.arange(0,22,1):
	matrix = np.load(T+"connectivity_matrix_seed_"+str(seed)+".npy")
	degree_counts = indegree(matrix)

	means.append(np.mean(degree_counts[0:1000]))
	stds.append(np.std(degree_counts[0:1000]))


np.save("eta_mean_degree.npy",means)
np.save("eta_std_degree.npy",stds)
