# Sodium Distribution around D72

This script visualizes the 3D spatial distribution of sodium ions relative to residue D72 across an MD trajectory using MDAnalysis.

## Description

The script:

- loads the structure file `step5_input.gro` and trajectory file `step7_filtered_skip50_Set_0_0_1.xtc`
- selects all sodium ions (`SOD`) and the D72 sidechain oxygens (`OD1`, `OD2`)
- computes the average position of the D72 sidechain oxygens for each frame
- accumulates sodium coordinates and D72 center positions over the trajectory
- recenters all coordinates using the mean sodium cloud position
- generates a 3D scatter plot of sodium positions and D72 positions
- saves the figure as a PNG image

## Input Files

- `step5_input.gro`
- `step7_filtered_skip50_Set_0_0_1.xtc`

## Output Files

- `sodium_distribution_with_D72.png`

## Requirements

- Python
- MDAnalysis
- NumPy
- Matplotlib

## Usage

```bash
python sodium_distribution_d72_visualization.py
