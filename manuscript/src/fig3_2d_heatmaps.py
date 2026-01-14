import matplotlib.pyplot as plt
import numpy as np

nx, ny = 5, 11  # AP x ML slice (z-middle)
gj_levels = [0.2, 0.5, 2.0]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for i, gj in enumerate(gj_levels):
    spread = 1.0 + 0.4 * np.log(gj/0.2)
    vmem_r = -45 * spread
    vmem_c = -20 + 5*(gj/2.0)
    
    # 2D Vmem heatmap (mid-DV plane)
    X, Y = np.meshgrid(np.arange(nx), np.arange(ny))
    Vmem = np.linspace(vmem_r, vmem_c, nx)[:, np.newaxis] * np.ones(ny)
    
    im = axes[i].imshow(Vmem, cmap='RdBu_r', vmin=-55, vmax=-15)
    axes[i].set_title(f'gj={gj}nS/pF\nRostral {vmem_r:.1f}mV → Caudal {vmem_c:.1f}mV')
    plt.colorbar(im, ax=axes[i], label='Vmem (mV)')

plt.tight_layout()
plt.savefig('fig3_2d_gap_junction_heatmaps.png', dpi=300, bbox_inches='tight')
plt.close()
print("✅ Fig.3 2D heatmaps generated")
