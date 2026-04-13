# Crosslinking Residue Pair Distance Analysis and Yield-Based Visualization

This workflow measures selected inter-chain residue distances from a set of PDB structures using MDAnalysis, then parses those distance files, matches residue pairs to experimental yield values, and generates subset-specific distance plots colored by yield.

## Description

The workflow:

- loads multiple PDB files in a specified order
- processes each structure individually
- measures distances between predefined residue pairs across **Chain A** and **Chain B**
- selects either `CA` or `CB` atoms depending on the residue
- converts residue names from three-letter codes to one-letter codes for reporting
- writes all measured distances to a separate text file for each input PDB
- reads multiple distance `.txt` files in the current directory
- skips the experimental yield file itself
- parses residue-pair distance values from each distance file
- parses experimental yield percentages from `experimental_yields.txt`
- maps residue pairs to predefined subsets:
  - **ICL**
  - **C-terminus**
- generates horizontal strip plots of distance distributions
- colors each residue pair according to its associated experimental yield
- saves one PNG file for each subset and input file

## Input Files

The workflow expects the following input files:

### PDB files
- `m134_final.pdb`
- `m162_final.pdb`
- `m164_final.pdb`
- `m181_final.pdb`

### Required yield file
- `experimental_yields.txt`

### Distance files
- `distance_values_1.txt`
- `distance_values_2.txt`
- `distance_values_3.txt`
- `distance_values_4.txt`

The distance files are expected to contain lines formatted like:

```text
Resid 281 (X-CB, Chain A) -> Resid 152 (Y-CB, Chain B) : 8.532 Å
