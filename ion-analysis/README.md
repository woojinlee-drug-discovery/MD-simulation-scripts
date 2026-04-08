# Ion Analysis

This folder contains MDAnalysis scripts for analyzing ion-related interactions in molecular dynamics simulations.

## Scripts

### `d72_sodium_distance_analysis.py`
This script calculates the minimum distance between residue 72 (D72) carboxylate oxygens (`OD1`, `OD2`) and any sodium ion (`SOD`) over the course of an MD trajectory.

#### Input
- `step5_input.gro`
- `step7_filtered_skip50_Set_0_0_0.xtc`

#### Output
- `D72_SOD_distances_anysodium.txt`
- `d72_sod_distance_anysodium.png`

#### What it does
- loads the structure and trajectory
- selects D72 carboxylate oxygens
- selects all sodium ions
- calculates the minimum D72–Na+ distance for each frame
- saves the distance values to a text file
- generates a distance vs time plot

#### Requirements
- Python
- MDAnalysis
- NumPy
- Matplotlib

#### Usage
```bash
python d72_sodium_distance_analysis.py
