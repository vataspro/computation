import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

#def xdot(x,y,z,t,sigma,rho,beta):
#	return (sigma*(y-x))

#def ydot(x,y,z,t,sigma,rho,beta):
#	return (x*(rho-z)-y)

#def zdot(x,y,z,t,sigma,rho,beta)

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


mpl.rcParams['legend.fontsize'] = 10

fig = plt.figure()
ax = fig.gca(projection='3d')
#theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#z = np.linspace(-2, 2, 100)
#r = z**2 + 1
#x = r * np.sin(theta)
#y = r * np.cos(theta)

t = np.linspace(0,T,N)
X = np.zeros((3,N))

X[:,0] = np.random.rand(3)


for i in range(1,N):
	k1 = dt * Xdot( X[:, i-1], t[i-1], sigma, rho, beta)
	k2 = dt * Xdot( X[:, i-1]+k1/2, t[i-1]+dt/2, sigma, rho, beta)
	k3 = dt * Xdot( X[:, i-1]+k2/2, t[i-1]+dt/2, sigma, rho, beta)
	k4 = dt * Xdot( X[:, i-1]+k3, t[i-1]+dt, sigma, rho, beta)

	X[:,i] = X[:,i-1] + (1/6)*np.transpose(np.array(((k1 + 2*k2 + 2*k3 + k4))))


ax.plot(X[0,:], X[1,:], X[2,:], label='Lorentz Attractor')
ax.legend()

plt.show()
