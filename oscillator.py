import numpy as np
import matplotlib.pyplot as plt

def func(x):
    k=5
    beta = 1
    return np.array(([0,1],[-k,beta])).dot(x)

N=1000
T=15
dt=float(T/N)

x_graph=np.zeros(N)
y_graph=np.zeros(N)


x=np.zeros((N,2))
x[0][0]=5
x_graph[0]=x[0][0]
y_graph[0]=x[0][1]


for i in range(1,N):
    k1 = func(x[i-1])*dt
    k2 = func(x[i-1]+k1/2)*dt
    k3 = func(x[i-1]+k2/2)*dt
    k4 = func(x[i-1]+k3)*dt

    x[i]=x[i-1]+float(1/6)*(k1+2*k2+2*k3+k4)

    x_graph[i]=x[i][0]
    y_graph[i]=x[i][1]

print(x)

plt.plot(x_graph,y_graph)
plt.show()
