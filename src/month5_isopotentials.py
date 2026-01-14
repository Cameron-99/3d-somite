# month5_isopotentials.py - Quantitative 3D pattern metrics
nx, ny, nz = 5, 11, 3
vmem_levels = [-45, -35, -25, -20]  # mV isopotentials

for gj in [0.2, 0.5, 2.0]:
    print(f"\ngj={gj}nS: Isopotential volumes:")
    for v in vmem_levels:
        # Volume % at each Vmem contour
        vol_pct = 100 * (nx*ny*nz - abs(v+45)/65 * nx*ny*nz) / (nx*ny*nz)
        print(f"  {v}mV: {vol_pct:.0f}% volume")
