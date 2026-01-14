import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(111, projection='3d')

# 154-cell 3D somite stack (125μm × 5μm)
x = np.linspace(0, 125, 154)
y = np.linspace(0, 125, 154)
X, Y = np.meshgrid(x, y)
Z = np.zeros_like(X)

# GREY PLANE AT Z=0.5 (mid-somite height)
ax.plot_surface(X, Y, Z+0.5, alpha=0.3, color='grey', 
                label='Somite mid-plane (z=0.5μm)')

# 3D AXES with somite dimensions
ax.plot([0,125],[0,0],[0,0], 'k-', lw=3, label='AP axis (125μm)')
ax.plot([0,0],[0,125],[0,0], 'k--', lw=2, label='ML axis')
ax.plot([0,0],[0,0],[0,5], 'r-', lw=3, label='Height (5μm)')

ax.text(130, 62.5, 2.5, '154-cell 3D Somite Stack', fontsize=14, 
        bbox=dict(facecolor='white', alpha=0.8))
ax.set_xlabel('AP Axis (μm)', fontsize=12)
ax.set_ylabel('ML Axis (μm)', fontsize=12) 
ax.set_zlabel('Height (μm)', fontsize=12)
ax.legend()

plt.tight_layout()
plt.savefig('fig1a_3d_axis_grey_plane.png', dpi=300, bbox_inches='tight')
plt.show()
