#~~***$ alexi's numpy Lorentz Attractor $***~~
#		12 Oct 2018
#Lorentz Attractor is a set of 3 coupled nonlinear equations that exhibit chaotic behaviour.
#In this code we initalise the starting positions and parameters (σ,ρ,β) with random numbers, and
#then numerically solve using Runge-Kutta of order 4.

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#This is the 3 coupled differential equations describing our Lorentz Attractor
def Xdot(X,t,sigma,rho,beta):
	D = np.zeros(3)
	D[0] = (sigma*(X[1]-X[0]))
	D[1] = (X[0]*(rho-X[2])-X[1])
	D[2] = (X[0]*X[1]-beta*X[2])
	return D

#Program constants: Size and Time
N = 100000
T = 10000
dt = float(T/N)

#Attractor constants
sigma = 5*np.random.rand()
rho = 5*np.random.rand()
beta = 5*np.random.rand()

#Figure parameters
mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')

#Initialise the starting conditions
t = np.linspace(0,T,N)
X = np.zeros((3,N))

X[:,0] = np.random.rand(3)


#Solve the system using RK4
for i in range(1,N):
	k1 = dt * Xdot( X[:, i-1], t[i-1], sigma, rho, beta)
	k2 = dt * Xdot( X[:, i-1]+k1/2, t[i-1]+dt/2, sigma, rho, beta)
	k3 = dt * Xdot( X[:, i-1]+k2/2, t[i-1]+dt/2, sigma, rho, beta)
	k4 = dt * Xdot( X[:, i-1]+k3, t[i-1]+dt, sigma, rho, beta)

	X[:,i] = X[:,i-1] + (1/6)*np.transpose(np.array(((k1 + 2*k2 + 2*k3 + k4))))


#Plot the solution
ax.plot(X[0,:], X[1,:], X[2,:], label='Lorentz Attractor')
ax.legend()

plt.show()
