from sys import argv

files = argv[1:]
first = True
outname = "merged_SID-RMSD.csv"

def write_out(line):
    global first
    global outname
    if first:
        mode = "w"
    else: 
        mode = "a"
    with open(outname, mode) as out:
        out.write(line)
 

def get_last_frame():
    global outname
    with open(outname, 'r') as out:
        return int(out.readlines()[-1].split(',')[0])

for f in files:
    if first:
        with open(f, 'r') as g:
            write_out(g.read())
        first = False
        continue
    last = get_last_frame()
    with open(f, 'r') as g:
        for line in g:
            if line[0] == "#" or line[0] == "f" or int(line.split(',')[0]) + last == last:
                continue
            line = line.split(',')
            line[0] = str(int(line[0]) + last)
            line = ','.join(line)
            write_out(line)    
