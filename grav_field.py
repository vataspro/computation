# Last Edit: alexi @ 15 Oct 2018
# Point particle in a gravitational field - this could also be an EM field
#since they both have the form (1/r)^2 .
# We set the field's source at r=0
import numpy as np
import matplotlib.pyplot as plt

N=1000
T=10
#Force constant:
#Changing this to negative represents a repuslive force
#so this could also be an EM field.
kappa = 10

dt=float(T/N)

rho = np.zeros(N)
vrho = np.zeros(N)
theta = np.zeros(N)
vtheta = np.zeros(N)
x = np.zeros(N)
y = np.zeros(N)


#Set the initial values for the radial distance and velocity
rho[0] = 10
vrho[0] = 0

theta[0] = 0
vtheta[0] = 10

for i in range(1,N):
    #Radial part
    rho[i] = rho[i-1]+vrho[i-1]*dt
    vrho[i] = vrho[i-1] - kappa*(1/(rho[i-1]**2))
    #Angular part
    theta[i] = theta[i-1]+vtheta[i-1]*dt
    vtheta[i] = vtheta[i-1] + 0*dt


for i in range(N):
    if rho[i]<0:
        rho[i]=0
    x[i]=rho[i]*(np.cos(theta[i]))
    y[i]=rho[i]*(np.sin(theta[i]))


plt.plot(x,y)
plt.show()
