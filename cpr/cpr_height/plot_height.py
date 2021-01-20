from matplotlib import pyplot as plt

colors = ["#006E6E", "#8C9196", "#D20537"]
alpha = 0.25
input_files = [
	"height_redox10.csv",
	#"height_main_rep2.csv",
	#"height_main_rep3.csv"
]
n_plots = len(input_files)


def read_height(input_file):
	data = []
	with open(input_file, "r") as f:
		f.readline()
		data = [line.strip().split(',') for line in f]

	time = [float(d[0]) / 1000 for d in data]
	height_auto = [float(d[1]) for d in data]
	height_man = [float(d[2]) for d in data]
	return time, height_auto, height_man


def mean(data):
	return sum(data) / len(data)


def running_mean(data, window):
	half_window = int(window / 2)
	prependix = [data[0] for i in range(half_window)]
	appendix = [data[-1] for i in range(half_window)]
	data_new = prependix + data + appendix
	data_out = []
	for i in range(0, len(data)):
		window_data = data_new[i:i + 2 * half_window + 1]
		data_out.append(mean(window_data))
	return data_out


### Read data
time = []
height_auto = []
height_man = []
for f in input_files:
	t, ha, hm = read_height(f)
	time.append(t)
	height_auto.append(ha)
	height_man.append(hm)


### Plot data
#plt.figure(figsize=(9.4, 4.8))
#plt.subplots_adjust(bottom=0.1, top=0.85, hspace=0.002)

# RMSF
fig, ax = plt.subplots()
for i in range(n_plots):
	ax.plot(time[i], height_auto[i], color=colors[i], alpha=alpha)
	ax.plot(time[i], running_mean(height_auto[i], 101), color=colors[i])
ax.set_xlim(0, max([t for time_series in time for t in time_series]))
ax.set_ylabel(r'Distance [$\mathrm{\AA}$]')
ax.set_xlabel('Time [ns]')

plt.tight_layout()
#x, y, w, h = ax3.get_position().bounds
#ax3.set_position([x, y+0.13, w, h])
#x, y, w, h = ax4.get_position().bounds
#ax4.set_position([x, y+(0.13 * 2), w, h])
#x, y, w, h = ax1.get_position().bounds
#ax1.set_position([x, y+0.13, w, h])

plt.savefig("CPR_height_FADox-FMNsq.png", dpi=1200)

plt.show()
