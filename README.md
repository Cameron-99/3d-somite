# 3D BETSE Somite Segmentation  
**Robust 3D Scaling of HCN2 Somite Patterning Through Cx43 Gap Junction Coupling**  
*Developmental Dynamics* (Submitted Jan 21, 2026) [ScholarOne Confirmation].

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
