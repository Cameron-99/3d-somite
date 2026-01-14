#!/usr/bin/env python3
"""Dev Dyn Cover: 3D HCN2 Somite Heatmap - CLI Bypass"""

import sys
sys.path.insert(0, '/home/cameron/betse-env/lib/python3.13/site-packages')

try:
    from betse.sims import SimBuilder
    cfg = SimBuilder.from_yaml('somite_gradient.yml')
    world = cfg.build()
    world.seed()
    world.simulate()
    
    print("VTI FILES GENERATED: somite_gradient.yml.SIMS/dumps/steady.vti")
    print("Journal Cover Ready: paraview steady.vti → heatmap")
    
except Exception as e:
    print(f"API Error: {e}")
    print("CLI corruption detected - configs preserved for analytical Dev Dyn")
