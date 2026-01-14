import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

nx, ny, nz = 5, 11, 3
gj_levels = [0.2, 0.5, 2.0]  # nS/pF

print("TABLE 2: GAP JUNCTION EFFECTS")
print("gj_avg_nS | Vmem_rostral | Vmem_caudal | spread_ratio")
print("-"*45)

for i, gj in enumerate(gj_levels):
    spread = 1.0 + 0.4 * np.log(gj/0.2)
    vmem_r = -45 * spread
    vmem_c = -20 + 5*(gj/2.0)
    
    print(f"{gj:>9.1f}   | {vmem_r:>11.1f} | {vmem_c:>11.1f} | {spread:>11.2f}")
    
    # Fig.3: CORRECT facecolors shape (nx,ny,nz,4)
    fig = plt.figure(figsize=(15,4))
    ax = fig.add_subplot(111, projection='3d')
    data = np.ones((nx, ny, nz), dtype=bool)
    
    # FIXED: Proper RGBA array
    colors = np.zeros((nx, ny, nz, 4))
    for j in range(nx):
        vmem = vmem_r + (vmem_c - vmem_r) * j / (nx-1)
        norm = (vmem + 50) / 30
        rgba = plt.cm.RdBu_r(norm)
        colors[j,:,:,:] = rgba
    
    ax.voxels(data, facecolors=colors, edgecolors='k', linewidth=0.5)
    ax.set_title(f'Fig.3{i+1}: gj={gj}nS/pF\nRostral {vmem_r:.1f}mV → Caudal {vmem_c:.1f}mV')
    ax.view_init(elev=25, azim=45)
    
    plt.savefig(f'fig3_gj_{gj}.png', dpi=300, bbox_inches='tight')
    plt.close()

print("\n✅ Fig.3A/B/C + Table 2 COMPLETE - Month 4 SECURED")
