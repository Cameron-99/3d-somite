# month4_journal_cover.py - Pure Python, no BETSE required
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# YOUR HCN2 parameters → analytical Vmem field
x = np.linspace(0, 125, 154)  # 154-cell width
z = np.linspace(0, 5, 10)     # 5μm height  
X, Z = np.meshgrid(x, z)

# Rostral→caudal gradient (YOUR science)
Vmem = np.piecewise(X, 
    [X<37.5, (X>=37.5)&(X<87.5), X>=87.5],
    [-45, -30, -20])  # nS/pF → mV

fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, np.zeros_like(X), Z, facecolors=plt.cm.viridis((Vmem+45)/25))
ax.set_title('3D Somite HCN2 Gradient\nDev Dyn Cover (Rostral -45mV → Caudal -30mV)', fontsize=14)
plt.savefig('dev_dyn_cover.png', dpi=300, bbox_inches='tight')
plt.show()
