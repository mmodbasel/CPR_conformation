from schrodinger.application.desmond.packages import traj, topo, analysis
from sys import argv

cms_file = argv[1]
trj_file = argv[2]

msys_model, cms_model = topo.read_cms(cms_file)
trj = traj.read_traj(trj_file)

protein_aids = cms_model.select_atom("chain.name A and res.num 76-677")
protein_gids = topo.aids2gids(cms_model, protein_aids, include_pseudoatoms=False)
radg_analyzer = analysis.Gyradius(msys_model, cms_model, gids=protein_gids)

ligand_aids = cms_model.select_atom("res.ptype FMN or res.ptype FAD")
ligand_st = cms_model.extract(ligand_aids)
ligand_gids = topo.aids2gids(cms_model, ligand_aids, include_pseudoatoms=False)


def distance(atom1, atom2):
	return ((atom1.x - atom2.x) ** 2 + (atom1.y - atom2.y) ** 2 + (atom1.z - atom2.z) ** 2) ** 0.5


distances = []
radgs = []
for i, frame in enumerate(trj):
	# Print progress
	if (i + 1) % 100 == 0:
		print(f"[*] Analyzing frame {i + 1} of {len(trj)}...")

	# Get distance between atoms
	ligand_st.setXYZ(frame.pos(ligand_gids))
	c8m = [atom for atom in ligand_st.atom if atom.pdbname.strip() == "C8M"]
	distances.append(distance(c8m[0], c8m[1]))

	# Get radius of gyration
	radg = analysis.analyze([frame], radg_analyzer)[0]
	radgs.append(radg)

# Write the results to file
try:
	out_file = argv[3] if argv[3][-4:] == ".csv" else argv[3] + ".csv"
except IndexError:
	out_file = "SEA_out.csv"

with open(out_file, "w") as f:
	f.write("Distance_FMN-FAD,RadG\n")
	for dist, radg in zip(distances, radgs):
		f.write(f"{dist},{radg}\n")

print(f"[+] Results written to {out_file}")

