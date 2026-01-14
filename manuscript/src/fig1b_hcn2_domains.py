# fig1b_hcn2_domains.py - COMPLETE HCN2 DOMAINS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(111, projection='3d')

# 5×11×3 somite = 165 cells (matches Fig.1A)
nx, ny, nz = 5, 11, 3
data = np.ones((nx, ny, nz), dtype=bool)

# HCN2 CONDUCTANCE DOMAINS (nS/pF)
domain_colors = np.zeros((nx, ny, nz, 4))
for i in range(nx):  # AP axis (rostral→caudal)
    for j in range(ny):  # ML axis
        for k in range(nz):  # DV axis
            if i < 2:           # Rostral: 1.2 nS/pF
                domain_colors[i,j,k] = [0.1,0.3,1.0,0.9]  # Blue
            elif i > 3:         # Caudal: 0.3 nS/pF
                domain_colors[i,j,k] = [1.0,0.2,0.1,0.9]  # Red
            else:               # Flank: 0.1 nS/pF
                domain_colors[i,j,k] = [0.2,1.0,0.2,0.9]  # Green

ax.voxels(data, facecolors=domain_colors, edgecolors='k', linewidth=0.5)
ax.set_xlabel('AP axis (rostral→caudal)', fontsize=14)
ax.set_ylabel('ML axis', fontsize=14)
ax.set_zlabel('DV height (3 layers)', fontsize=14)
ax.set_title('Fig.1B: HCN2 Conductance Domains 3D\nRostral(1.2nS)→Flank(0.1nS)→Caudal(0.3nS)', fontsize=16)
ax.view_init(elev=25, azim=45)

plt.tight_layout()
plt.savefig('fig1b_hcn2_domains.png', dpi=300, bbox_inches='tight')
plt.show()
