# Last edit: alexi @ 15 Oct 2018
#  Random walk code - plots the final distance from the starting location
# as a function of the number of steps. Obviously this is still random.

import numpy as np
import matplotlib.pyplot as plt

# K is the number of "experiments"
K=100
x = np.arange(K)
N = np.zeros(K)

for i in range(K):
	for j in range(i):
		if np.random.random() > float(1/2):
			N[i] = N[i] + 1
		else:
			N[i] = N[i] - 1

plt.plot(x,N)
plt.show()



