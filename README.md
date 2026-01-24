# 3D BETSE Somite Segmentation  
**Robust 3D Scaling of HCN2 Somite Patterning Through Cx43 Gap Junction Coupling**  
*Developmental Dynamics* (Submitted Jan 21, 2026) [ScholarOne Confirmation].
Production data used 1440×1920×10 voxel stacks (125×125×5 μm voxels; 27.6 M total voxels) representing 
DV-compressed epithelial somites stacked rostrocaudally from a validated 165-cell single-somite geometry. 
Cell occupancy was 10.2% of voxels (2.82M somatic cells), reflecting epithelial shell volume plus 
physiological inter-somite extracellular space [2.82M cells = 27.6M voxels × 0.102 occupancy]. 
HCN2 partitioning followed validated 2D assays (rostral high to caudal low conductance).

![Main Result](figs/Fig10_ten-somite-stack.png)  
**Key Discovery**: Epithelial geometry (2.5:1 DV compression) drives **3.4× Cx43 electrotonic amplification** + **1.7× dermomyotome Vmem domain expansion** vs 2D models.

## ⚡ Quick Start
```bash
# Clone + install (LMDE 7/Ubuntu 24.04)
git clone https://github.com/Cameron-99/3D-BETSE-Somite.git
cd 3D-BETSE-Somite
pip install -r requirements.txt  # BETSE + analysis
betse sim.toml                  # Single somite validation
betse stack.toml                # 10-somite stack (2.8M cells)
python somiteanalysisfinal.py   # Figs 1-10 TIFFs → ~/Desktop/
