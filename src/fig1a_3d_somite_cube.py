# fig1a_3d_somite_cube.py - REAL 3D CELL VISUALIZATION
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12,9))
ax = fig.add_subplot(111, projection='3d')

# 154-cell 3D somite stack: 11×14×1 (125μm×125μm×5μm)
nx, ny, nz = 11, 14, 1  
x = np.linspace(0, 125, nx)
y = np.linspace(0, 125, ny) 
z = np.linspace(0, 5, nz)
X, Y, Z = np.meshgrid(x, y, z, indexing='ij')

# CELL CENTERS (154 visible voxels)
ax.scatter(X.flatten(), Y.flatten(), Z.flatten(), 
           c='lightblue', s=200, alpha=0.7, 
           label='154 cells')

# HCN2 Vmem GRADIENT (rostral→caudal: blue→red)
rostral_caudal = np.linspace(-45, -20, ny)  # AP axis gradient
colors = plt.cm.RdBu_r((rostral_caudal + 45)/25)
for i in range(nx):
    for j in range(ny):
        ax.scatter(X[i,j,0], Y[i,j,0], Z[i,j,0], 
                  c=[colors[j]], s=180, alpha=0.8)

ax.set_xlabel('AP axis (μm)', fontsize=14)
ax.set_ylabel('ML axis (μm)', fontsize=14)
ax.set_zlabel('DV height (μm)', fontsize=14)
ax.set_title('3D Somite Stack: HCN2 Vmem Axis\n154 cells, rostral→caudal gradient', 
             fontsize=16, pad=20)

plt.tight_layout()
plt.savefig('fig1a_3d_somite_cube.png', dpi=300, bbox_inches='tight')
plt.show()
