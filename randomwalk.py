# Last edit: alexi @ 15 Oct 2018
# Random walk code.

import numpy as np
import matplotlib.pyplot as plt

# K is the number of "experiments"
K=10000
# N is the number of steps in each "experiment"
N=1000

x = np.zeros((K,N))
Nu = np.zeros(K)
Num = 0

for i in range(K):
    for j in range(N):
#	 Since np.random.random() gives a uniformly distributed random number in [0,1]
#	we take a probability of (1/2) for either a positive or a negative step.
        if np.random.random() > float(1/2):
            x[i][j]=x[i][j]+1
        else:
            x[i][j]=x[i][j]-1

        Nu[i]=Nu[i]+x[i][j]
    Nu[i]=Nu[i]/N
    Num=Num+Nu[i]


plt.hist(Nu,bins=100)
plt.xlabel("Final location")
plt.show()



