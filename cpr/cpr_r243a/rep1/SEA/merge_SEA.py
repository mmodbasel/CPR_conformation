from sys import argv
import os

files = argv[1:]

filename = "merged.csv"
first = True

def write_out(line):
    global first
    if first:
        append_write = 'w'
        first = False
    else:
        append_write = 'a'
    with open(filename, append_write) as file_out:
        file_out.write(line)

orders = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]

with open(files[0], 'r') as file_in:
    for line in file_in:
        write_out(line)

for file, order in zip(files[1:], orders):
    with open(file, 'r') as f:
        for line in f:
            line = line[:-1]
            if line[0] == "#" or line[0] == "T":
                continue
            new_line = []
            for x in order:
                if x == "x":
                    new_line.append("")
                else:
                    new_line.append(line.split(',')[x])
            write_out(','.join(new_line) + "\n")
