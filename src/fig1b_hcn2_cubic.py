# fig1b_hcn2_cubic.py - 5×5×5 CUBES (matches Fig.1A)
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

nx, ny, nz = 5, 5, 5  # CUBIC - matches Fig.1A
data = np.ones((nx, ny, nz), dtype=bool)

# HCN2 DOMAINS: Rostral(1.2nS)→Flank(0.1nS)→Caudal(0.3nS)
colors = np.zeros((nx, ny, nz, 4))
for i in range(nx):  # AP axis ONLY
    if i < 2:         # Rostral
        colors[i,:,:,:] = [0.1,0.3,1.0,0.9]  # Blue
    elif i > 3:       # Caudal
        colors[i,:,:,:] = [1.0,0.2,0.1,0.9]  # Red
    else:             # Flank
        colors[i,:,:,:] = [0.2,1.0,0.2,0.9]  # Green

ax.voxels(data, facecolors=colors, edgecolors='k', linewidth=0.8)
ax.set_title('Fig.1B: HCN2 Conductance Domains (5×5×5)\nRostral(1.2nS)→Flank(0.1nS)→Caudal(0.3nS)', fontsize=16)
ax.view_init(elev=25, azim=45)

plt.savefig('fig1b_hcn2_cubic.png', dpi=300, bbox_inches='tight')
plt.show()
