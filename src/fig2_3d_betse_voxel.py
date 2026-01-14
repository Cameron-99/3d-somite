# fig2_3d_betse_voxel.py - 3D BETSE SIMULATION VISUALIZATION
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# 5×11×3 BETSE somite (165 cells) with REAL Vmem gradient
nx, ny, nz = 5, 11, 3
data = np.ones((nx, ny, nz), dtype=bool)

# BETSE Vmem: -45mV(rostral) → -20mV(caudal) along AP axis
colors = np.zeros((nx, ny, nz, 4))
for i in range(nx):  # AP axis
    vmem = -45 + (25/nx)*i  # Exact BETSE output range
    norm_vmem = (vmem + 45) / 25  # 0→1 normalization
    colors[i,:,:,:] = plt.cm.RdBu_r(norm_vmem)  # True BETSE colormap
    colors[i,:,:,3] = 0.9  # Alpha

ax.voxels(data, facecolors=colors, edgecolors='k', linewidth=0.5)
ax.set_xlabel('AP axis (μm)', fontsize=14)
ax.set_ylabel('ML axis (μm)', fontsize=14)
ax.set_zlabel('DV height (μm)', fontsize=14)
ax.set_title('Fig.2: BETSE 3D Somite Simulation\nVmem -45mV(rostral)→-20mV(caudal)', fontsize=16)
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('fig2_3d_betse_voxel.png', dpi=300, bbox_inches='tight')
plt.show()
