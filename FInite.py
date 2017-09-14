import numpy as np    # External library for numerical calculations
import matplotlib.pyplot as plt   # plotting library

plt.ion()


# Function defining the initial and analytic solution
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)

def plot(x,t, phi):
	plt.clf()
	# Plot the solution in comparison to the analytic solution
	plt.plot (x, initialBell(x - (dt/dx)*phi[j]*t), 'k', label = 'initial condition')
	plt.plot (x, phi, 'b', label = 'CTCS')
	plt.legend ( loc = 'best' )
	plt.xlabel ('x')
	plt.ylabel(' $\phi$ ')
	plt.axhline(0, linestyle =':', color ='red')
	plt.show()
	plt.pause(0.2)
        plt.savefig("finite_{0}.jpg".format( int(200*t) ))
	plt.close()

# Setup space, initial phi profile and Courant number
nx = 50      #number of points in space
c = 0.2       # THe Courant number
dt = 0.005
dx = 1./nx


# Spatial variable goin from zero to one inclusive
x = np.linspace (0.0, 1.0, nx+1)
# THree time levels of the dependent variable, phi

phi = initialBell (x)
phiNew = phi.copy()

nt = 50
# derive quantities
dt = 0.005
dx = 1./nx


# FCTS for the first time step
# loop over spce
for j in xrange( 1, nx ):
    phi [j] = phi [j] - 0.5*(dt/dx)*phi[j]*( phi[j+1] - phi[j-1] )

# apply periodic boundary conditions
phi [0] = phi [0] - 0.5*(dt/dx)*phi[j]*(phi[1] - phi[nx -1])
phi [nx] = phi[0]

# Loop over remaining time -step (nt) using CTCS
nt = 50
# derive quantities
dt = 0.005
dx = 1./nx


for n in xrange (0, nt):
    t= n*dt
	
    # loop over spce
    for j  in xrange ( 1, nx ):
        phiNew [j] = phi[j] - 0.5*(dt/dx)*phi[j]*( phi [j+1] - phi[j-1] )
    # apply perodic boundary conditions
    phiNew [0] = phi [0] - 0.5*(dt/dx)*phi[j]*( phi[1] - phi[nx-1] )
    phiNew [nx] = phiNew[0]
    # update phi for the nxet time - step
    phi= phi.copy()
    phi = phiNew.copy()
    plot(x,t, phi)























