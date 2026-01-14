import yaml
import numpy as np
import subprocess
from pathlib import Path
from deap import base, creator, tools, algorithms
import random

class BETSEController:
    def __init__(self, config_path="sim_config/sim_config.yml"):
        self.config_path = Path(config_path)
        self.results_path = Path("RESULTS/SIMS") / next(Path("RESULTS/SIMS").glob("20*")) / "pfields" / "vmem.npy"
    
    def perturb_drug(self, channel='hcn2', scale=0.5):
        """Block somite HCN2 (amiloride-like)"""
        with open(self.config_path) as f:
            config = yaml.safe_load(f)
        # Fix path for actual BETSE 1.5 structure
        config['network']['channels'][channel]['density']['somite'] *= scale
        with open(self.config_path, 'w') as f:
            yaml.dump(config, f, indent=2)
    
    def simulate(self):
        """Run BETSE → load Vmem"""
        subprocess.run(['betse', 'sim', str(self.config_path)], check=True)
        # BETSE 1.5 stores in RESULTS/latest/pfields/
        self.vmem = np.load(self.results_path)
    
    def compute_mse(self, target):
        return float(np.mean((self.vmem - target)**2))

def create_target_somite(shape=(15,15)):
    target = np.full(shape, -20.0)
    yy, xx = np.ogrid[:shape[0], :shape[1]]
    somite = ((xx-7.5)**2 + (yy-7.5)**2) < 3**2
    target[somite] = 25.0
    return target

print("BETSEController loaded ✓")
