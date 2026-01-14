# fig1a_3d_geometry.py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')

# 154-cell stack (125×5μm)
verts = [ [(0,0,0),(125,0,0),(125,5,0),(0,5,0)] ]  # Base
ax.add_collection3d(Poly3DCollection(verts, alpha=0.3, facecolor='gray'))
ax.text(62.5, 0, 2.5, '154-cell 3D Somite Stack\n125μm × 5μm', ha='center')

plt.savefig('fig1a_3d_geometry.png', dpi=300)
plt.show()
