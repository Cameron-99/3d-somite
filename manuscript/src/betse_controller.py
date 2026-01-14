import yaml, numpy as np, subprocess, glob
from pathlib import Path
from deap import base, creator, tools, algorithms
import random

class BETSEController:
    def __init__(self, config_path="sim_config/sim_config.yml"):
        self.config_path = Path(config_path)
    
    def get_latest_vmem(self):
        """Auto-find latest vmem.npy in RESULTS/SIMS/[timestamp]/pfields/"""
        sim_dirs = sorted(Path("RESULTS/SIMS").glob("20*"), reverse=True)
        if not sim_dirs:
            raise FileNotFoundError("No RESULTS/SIMS/20* directories found")
        vmem_path = sim_dirs[0] / "pfields" / "vmem.npy"
        if not vmem_path.exists():
            raise FileNotFoundError(f"vmem.npy not found: {vmem_path}")
        return np.load(vmem_path)
    
    def perturb_drug(self, channel='hcn2', scale=0.5):
        with open(self.config_path) as f:
            config = yaml.safe_load(f)
        config['network']['channels'][channel]['density']['somite'] *= scale
        with open(self.config_path, 'w') as f:
            yaml.dump(config, f, indent=2)
    
    def simulate(self):
        subprocess.run(['betse', 'sim', str(self.config_path)], check=True)
        self.vmem = self.get_latest_vmem()
    
    def compute_mse(self, target):
        # Resize to match simulation shape
        sim_shape = self.vmem.shape
        target_resized = np.array(target)
        if target_resized.shape != sim_shape:
            from scipy.ndimage import zoom
            target_resized = zoom(target_resized, sim_shape[0]/target_resized.shape[0])
        return float(np.mean((self.vmem - target_resized)**2))

def create_target_somite(shape=(15,15)):
    target = np.full(shape, -20.0)
    yy, xx = np.ogrid[:shape[0], :shape[1]]
    somite = ((xx-7.5)**2 + (yy-7.5)**2) < 3**2
    target[somite] = 25.0
    return target

print("BETSEController FIXED ✓ - Auto-detects RESULTS/SIMS paths")
