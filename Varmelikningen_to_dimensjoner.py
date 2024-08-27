import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 1.0  # Length of the square domain
Nx = Ny = 50  # Number of grid points in x and y directions
Nt = 200  # Number of time steps
alpha = 0.1055  # Thermal diffusivity

# Grid spacing
dx = dy = L / (Nx - 1)
dt = 0.001  # Time step size

# Initialize temperature field
u = np.zeros((Nx, Ny))  # Temperature at t=0
u[Nx//4:3*Nx//4, Ny//4:3*Ny//4] = 1.0  # Initial temperature distribution (for example)

# Perform time-stepping
for n in range(1, Nt + 1):
    # Create copies of the temperature field
    u_old = u.copy()

    # Update temperature field using implicit method
    for i in range(1, Nx - 1):
        for j in range(1, Ny - 1):
            u[i, j] = u_old[i, j] + alpha * dt * (
                    (u_old[i + 1, j] - 2 * u_old[i, j] + u_old[i - 1, j]) / dx ** 2 +
                    (u_old[i, j + 1] - 2 * u_old[i, j] + u_old[i, j - 1]) / dy ** 2)

# Plot the final temperature field
plt.imshow(u, extent=[0, L, 0, L], origin='lower', cmap='hot')
plt.colorbar(label='Temperature')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Temperature distribution after {} time steps'.format(Nt))
plt.show()
