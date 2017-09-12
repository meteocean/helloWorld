import numpy as np    # External library for numerical calculations
import matplotlib.pyplot as plt   # plotting library

plt.ion()

# Function defining the initial and analytic solution
def initialBell(x):
    return np.where(x%1. < 0.5, np.power(np.sin(2*x*np.pi), 2), 0)

def plot(x, u, t, phi):
	plt.clf()
	# Plot the solution in comparison to the analytic solution
	plt.plot (x, initialBell(x - u*t), 'k', label = 'analytic')
	plt.plot (x, phi, 'b', label = 'CTCS')
	plt.legend ( loc = 'best' )
	plt.xlabel ('x')
	plt.ylabel(' $\phi$ ')
	plt.axhline(0, linestyle =':', color ='red')
	plt.show()
	plt.pause(0.1)

# Setup space, initial phi profile and Courant number
nx = 40       #number of points in space
c = 0.2       # THe Courant number

# Spatial variable goin from zero to one inclusive
x = np.linspace (0.0, 1.0, nx+1)
# THree time levels of the dependent variable, phi
phi = initialBell (x)
phiNew = phi.copy()
phiOld = phi.copy()

# FCTS for the first time step
# loop over spce
for j in xrange( 1, nx ):
    phi [j] = phiOld [j] - 0.5*c*( phiOld [j+1] - phiOld[j-1] )

# apply periodic boundary conditions
phi [0] = phiOld [0] - 0.5*c*(phiOld[1] - phiOld[nx -1])
phi [nx] = phi[0]

# Loop over remaining time -step (nt) using CTCS
nt = 100
# derive quantities
u = 1.
dx = 1./nx
dt = c*dx/u

for n in xrange (1, nt):
    t= n*dt
	
    # loop over spce
    for j  in xrange ( 1, nx ):
        phiNew [j] = phiOld [j] - c*( phi [j+1] - phi[j-1] )
    # apply perodic boundary conditions
    phiNew [0] = phiOld [0] - c*( phi[1] - phi[nx-1] )
    phiNew [nx] = phiNew[0]
    # update phi for the nxet time - step
    phiOld = phi.copy()
    phi = phiNew.copy()
    plot(x, u, t, phi)























