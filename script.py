#!/usr/bin/python3
import os
infile = "/etc/apt/sources.list"
outfile = "/etc/apt/sources.list"
delete_list = ["# Kali linux repositories | Added by Katoolin\n", "deb http://h$
fin = open(infile)
os.remove("/etc/apt/sources.list")
fout = open(outfile, "w+")
for line in fin:
    for word in delete_list:
        line = line.replace(word, "")
    fout.write(line)
fin.close()
fout.close()
