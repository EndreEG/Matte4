import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Definer initialbetingelsene
def initial_condition(x, y):
    return 2 * np.sin(x) * np.sin(2 * y) + 3 * np.sin(4 * x) * np.sin(5 * y)

# Definer grenseverdier
Lx = Ly = np.pi
Nx = Ny = 50
T = 0.1
Nt = 1000
dx = Lx / (Nx - 1)
dy = Ly / (Ny - 1)
dt = T / Nt

# Initialisere grid og initialbetingelser
x = np.linspace(0, Lx, Nx)
y = np.linspace(0, Ly, Ny)
X, Y = np.meshgrid(x, y)
u = initial_condition(X, Y)

# Opprett figuren og aksen for animasjonen
fig, ax = plt.subplots()
plot = ax.contourf(X, Y, u, cmap='viridis')
plt.colorbar(plot, ax=ax, label='Temperatur')
ax.set_title('Tid: 0')

# Funksjon for å oppdatere plottet ved hver frame i animasjonen
def update(frame):
    global u
    for _ in range(10):  # Gjør flere iterasjoner per frame for å gjøre animasjonen raskere
        u[1:-1, 1:-1] = u[1:-1, 1:-1] + dt * ((u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2 +
                                               (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2)
    plot = ax.contourf(X, Y, u, cmap='viridis')
    ax.set_title('Tid: {:.2f}'.format(frame * dt * 10))  # Vis tiden for hver frame

# Opprett animasjonen
animation = FuncAnimation(fig, update, frames=Nt//10, interval=50)
plt.show()
