from matplotlib import pyplot as plt
from os import listdir

plot_name = "RMSF_metadynamics_wt.png"
color1, color2 = "#006E6E", "#D20537"
dat_file = "P_RMSF.dat"

with open(dat_file, "r") as f:
	f.readline()
	data = [float(line.strip().split()[5]) for line in f]

residues = [i + 67 for i in range(len(data))]

fig, ax = plt.subplots()
ax.plot(residues, data, color=color1)
plt.xlabel("Residue")
plt.ylabel(r"$\mathrm{RMSF~[\AA]}$")
plt.xlim(67, 677)
plt.tight_layout()
plt.savefig(plot_name, dpi=1200)
plt.show()
