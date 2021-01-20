from schrodinger.application.desmond.packages import analysis, traj, topo
from sys import argv
import matplotlib.pyplot as plt

cms_file = argv[1]
trajectory = argv[2]
outname = argv[3]

msys_model, cms_model = topo.read_cms(cms_file)
tr = traj.read_traj(trajectory)

glob_aids = cms_model.select_atom('chain.name A and res.num 67-677 and not atom.ele H')
glob_st = cms_model.extract(glob_aids)
glob_gids = topo.aids2gids(cms_model, glob_aids, include_pseudoatoms=False)

mem_aids = cms_model.select_atom('res.ptype POPC and not atom.ele H')
mem_st = cms_model.extract(glob_aids)
mem_gids = topo.aids2gids(cms_model, mem_aids, include_pseudoatoms=False)

com1 = analysis.Com(msys_model, cms_model, asl='chain.name A and res.num 67-677 and not atom.ele H')
com2 = analysis.Com(msys_model, cms_model, asl='res.ptype POPC and not atom.ele H')
distance = analysis.Distance(msys_model, cms_model, com1, com2)

results = analysis.analyze(tr, com1, com2, distance)
coms_prot, coms_mem, dists = results[0], results[1], results[2]

distances_auto = []
distances_man = []
times = []
for frame, com_prot, com_mem, dist in zip(tr, coms_prot, coms_mem, dists):
	distances_auto.append(float(dist))
	distance_man = abs(com_prot[2] - com_mem[2])
	distances_man.append(float(distance_man))
	times.append(frame.time)


with open(outname, "w") as f:
	f.write(f"Time,Height_auto,Height_man\n")
	for time, distance_auto, distance_man in zip(times, distances_auto, distances_man):
		f.write(f"{time},{distance_auto},{distance_man}\n")
