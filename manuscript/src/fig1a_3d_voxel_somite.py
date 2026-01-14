# fig1a_3d_cubic_somite.py - IDEALIZED 5×5×5 CUBES
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# 5×5×5 = 125 cubic cells (25μm³ each)
nx, ny, nz = 5, 5, 5
data = np.ones((nx, ny, nz), dtype=bool)

# HCN2 Vmem gradient: Rostral→caudal (AP axis = x)
colors = np.zeros(data.shape + (4,))
for i in range(nx):  # AP axis ONLY
    vmem = -45 + (25/nx)*i  # -45mV → -20mV
    if i < 2:           # Rostral
        colors[i,:,:,:] = [0.1,0.3,1.0,0.85]   # Blue
    elif i > 3:         # Caudal  
        colors[i,:,:,:] = [1.0,0.2,0.1,0.85]   # Red
    else:               # Mid
        colors[i,:,:,:] = [0.8,0.8,0.2,0.85]   # Yellow

# CUBIC VOXELS - idealized cells
ax.voxels(data, facecolors=colors, edgecolors='k', linewidth=0.8, alpha=0.9)

ax.set_xlabel('AP axis (rostral→caudal)', fontsize=14)
ax.set_ylabel('ML axis', fontsize=14)
ax.set_zlabel('DV height', fontsize=14)
ax.set_title('Fig.1A: 3D Somite (125 cubic cells)\nHCN2 Vmem axis formation', fontsize=16)
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('fig1a_3d_cubic_somite.png', dpi=300, bbox_inches='tight')
plt.show()
# fig1a_3d_voxel_somite.py - TRUE 3D CELL CUBE
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# REAL 3D somite: 5(AP) × 11(ML) × 3(DV) = 165 voxels
nx, ny, nz = 5, 11, 3  # AP × ML × DV
data = np.ones((nx, ny, nz), dtype=bool)

# HCN2 Vmem gradient: Rostral(high)=blue → Caudal(low)=red ALONG AP AXIS ONLY
colors = np.zeros(data.shape + (4,))
for i in range(nx):  # AP axis (rostral→caudal)
    vmem = -45 + (25/nx)*i  # -45mV → -20mV
    if vmem < -35:      # Rostral
        colors[i,:,:,0] = 0.1   # Blue R
        colors[i,:,:,1] = 0.3   # G  
        colors[i,:,:,2] = 1.0   # B
    elif vmem < -25:    # Mid
        colors[i,:,:,:] = [0.8, 0.8, 0.2, 0.9]  # Yellow
    else:               # Caudal
        colors[i,:,:,0] = 1.0   # Red R
        colors[i,:,:,1] = 0.2   # G
        colors[i,:,:,2] = 0.1   # B
    colors[i,:,:,3] = 0.85  # Alpha

# VOXEL PLOT - DISTINCT CELLS, NO COLOR MERGING
ax.voxels(data, facecolors=colors, edgecolors='k', linewidth=0.5, alpha=0.85)

ax.set_xlabel('AP axis (rostral→caudal)', fontsize=14)
ax.set_ylabel('ML axis', fontsize=14)
ax.set_zlabel('DV height (3 layers)', fontsize=14)
ax.set_title('3D Somite Stack: HCN2 Vmem Axis Formation\n165 voxels (5×11×3)', fontsize=16)

# Optimal viewing angle for cube perception
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('fig1a_3d_voxel_somite.png', dpi=300, bbox_inches='tight')
plt.show()
