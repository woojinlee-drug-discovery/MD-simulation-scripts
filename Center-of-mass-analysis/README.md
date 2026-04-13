# Center of Mass Distance Analysis

This script calculates the center of mass (COM) distance between the receptor and beta-arrestin from an MD trajectory using MDTraj.

## Script

- `COM_analysis_script.py`

## Description

The script:

- loads the structure file `step5_input.gro`
- loads the trajectory file `step7_filtered_skip50_Set_0_0_1.xtc`
- applies periodic boundary condition (PBC) correction using `image_molecules()`
- selects C-alpha atoms for:
  - receptor residues 1–434
  - beta-arrestin residues 435–796
- computes the center of mass of each group for every frame
- calculates the COM distance between receptor and beta-arrestin
- converts the distances from nanometers to Ångströms
- saves the results to a text file
- generates and saves a distance-vs-time plot

## Input Files

- `step5_input.gro`
- `step7_filtered_skip50_Set_0_0_1.xtc`

## Output Files

The script creates an output directory:

- `com_distance/`

Inside this folder, it saves:

- `com_distance_receptor_arrestin.txt`
- `com_distance_mdtraj_plot.png`

## Output Format

The text output file contains two columns:

1. Time (ns)
2. COM distance (Å)

Example:

```text
Time (ns)    COM Distance (Å)
0.0          28.4215
0.5          28.3178
1.0          28.5022
