COM_analysis_script.py

This script calculates the center of mass (COM) distance between the receptor (residues 1–434) and β-arrestin (residues 435–796) across a molecular dynamics trajectory using MDTraj, and generates both numerical and graphical outputs.

Description

The script:

loads the structure (.gro) and trajectory (.xtc) files
applies periodic boundary condition (PBC) corrections using image_molecules()
selects C-alpha atoms for:
receptor (residues 1–434)
β-arrestin (residues 435–796)
extracts atomic masses from the MDTraj topology
computes the center of mass (COM) for each group in every frame
calculates the Euclidean distance between receptor and arrestin COMs per frame
converts distances from nanometers to Ångströms
generates a time array (in ns) corresponding to trajectory frames
saves COM distance values to a text file
generates and saves a COM distance vs time plot
Input Files
step5_input.gro
step7_filtered_skip50_Set_0_0_1.xtc
Output Files

Saved in ./com_distance/:

com_distance_receptor_arrestin.txt
→ Contains time (ns) and COM distance (Å)
com_distance_mdtraj_plot.png
→ COM distance vs time plot
Output Format

The output text file contains two columns:

Time (ns)    COM Distance (Å)
0.0          32.145
0.5          31.982
1.0          31.756
...
Requirements
Python
MDTraj
NumPy
Matplotlib
tqdm
Usage
python com_distance_mdtraj.py
