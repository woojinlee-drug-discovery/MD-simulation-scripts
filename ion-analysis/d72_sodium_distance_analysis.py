import MDAnalysis as mda
from MDAnalysis.analysis.distances import distance_array
import numpy as np
import matplotlib.pyplot as plt

# Load the universe
u = mda.Universe('step5_input.gro', 'step7_filtered_skip50_Set_0_0_0.xtc')

# Select atoms of interest: Residue 72 (D72) and all sodium ions (SOD)
d72_atoms = u.select_atoms('resid 72 and (name OD1 or name OD2)')  # Select carboxylate oxygens in D72
sodium_atoms = u.select_atoms('resname SOD')  # Select all sodium ions

# Prepare to store distances and time
distances_d72_sod = []
time_ns = []

# Calculate distances between selected atoms over time
for ts in u.trajectory:
    dist_d72_sod = distance_array(d72_atoms.positions, sodium_atoms.positions, box=ts.dimensions)
    min_dist_d72_sod = dist_d72_sod.min()  # Find the minimum distance to any sodium ion
    
    distances_d72_sod.append(min_dist_d72_sod)
    time_ns.append(u.trajectory.time / 1000)  # Convert time from ps to ns

# Convert lists to numpy arrays
distances_d72_sod = np.array(distances_d72_sod)
time_ns = np.array(time_ns)

# Save the results to a text file
np.savetxt("D72_SOD_distances_anysodium.txt", distances_d72_sod, fmt="%0.4f", header="Closest distances between D72 and SOD over frames")

# Plot the distance between D72 and sodium
plt.figure(figsize=(12, 8))
plt.plot(time_ns, distances_d72_sod, label='D72-SOD Distance', color='blue')

plt.xlabel('Time (ns)')
plt.ylabel('Distance (Å)')
plt.title('Distance between D72 and Sodium (SOD) over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('d72_sod_distance_anysodium.png')
plt.show()

print("Distance analysis complete. Results saved to D72_SOD_distances.txt and d72_sod_distance.png.")

