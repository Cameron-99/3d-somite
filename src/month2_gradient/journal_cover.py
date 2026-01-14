import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# YOUR HCN2 gradient → 3D Vmem heatmap (154-cell stack)
x = np.linspace(0, 125, 154)  # 125μm width
z = np.linspace(0, 5, 10)     # 5μm height
X, Z = np.meshgrid(x, z)

# Rostral→caudal gradient (1.2→0.3→0.1 nS/pF)
Vmem = np.piecewise(X, [X<37.5, (X>=37.5)&(X<87.5), X>=87.5], 
                   [-45, -37.5, -20])  # YOUR science

fig = plt.figure(figsize=(10,6))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, np.zeros_like(X), Z, facecolors=plt.cm.viridis((Vmem+45)/25*255),
                      shade=True, cmap='viridis')
ax.set_title('3D Somite Bioelectric Axis\nRostral HCN2:1.2nS (-45mV) → Caudal HCN2:0.3nS (-30mV)', 
             fontsize=12, pad=20)
ax.set_xlabel('AP Axis (μm)')
ax.set_zlabel('Height (μm)')
plt.tight_layout()
plt.savefig('dev_dyn_cover.png', dpi=300, bbox_inches='tight')
plt.show()
