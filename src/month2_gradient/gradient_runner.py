#!/usr/bin/env python3
"""Month 2: Rostral-Caudal HCN2 Gradient - TOTAL CLI BYPASS"""

import subprocess
import sys
import os

# Full path isolation - no inherited state
betse_path = '/home/cameron/betse-env/bin/betse'
config = 'somite_gradient.yml'

# Nuclear clean first
subprocess.run(['rm', '-rf', f'{config}.*'], check=False)

# Subprocess spawn FRESH CLI instances (serpent-proof)
print("Seeding 154-cell 3D rostral-caudal somite...")
result1 = subprocess.run([betse_path, 'seed', config], 
                        capture_output=True, text=True)
print(result1.stdout)

print("Simulating HCN2 gradient...")
result2 = subprocess.run([betse_path, 'sim', config], 
                        capture_output=True, text=True)  
print(result2.stdout)

print("MONTH 2 COMPLETE: Check somite_gradient.yml.SIMS/dumps/steady.vti")
