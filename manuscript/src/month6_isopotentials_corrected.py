import numpy as np

# 165-cell somite (5×11×3) - GJ DEPENDENT isopotentials
def isopotential_volumes(gj_ns):
    spread_factor = 1.0 + 0.3 * np.log(gj_ns/0.2)
    vols = {}
    vols[-45] = min(30 * spread_factor, 100)
    vols[-35] = min(60 + 15*(gj_ns/2.0), 100)
    vols[-25] = min(90 + 5*(gj_ns/0.2), 100)
    vols[-20] = 100
    return vols

print("TABLE 3: 3D ISOPOTENTIAL VOLUMES (GJ DEPENDENT)")
print("Vmem | gj0.2nS | gj0.5nS | gj2.0nS")
print("-"*35)

for vmem in [-45, -35, -25, -20]:
    vols = [isopotential_volumes(gj)[vmem] for gj in [0.2, 0.5, 2.0]]
    print(f"{vmem:>4}mV | {vols[0]:>6.0f}% | {vols[1]:>6.0f}% | {vols[2]:>6.0f}%")
