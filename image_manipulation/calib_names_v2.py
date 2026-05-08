#!/usr/bin/env python3
import os
from os.path import isfile, join
import sys


D_option = sys.argv[1]
all_files = [f for f in os.listdir(".") if isfile(join(".", f)) if f[-5:] == ".tiff" and f[0:4] == "i22-"]
all_files.sort()
prefix = []
for i in range(len(all_files)):
    if i < 10:
        prefix.append("0000" + str(i))
    elif i < 100:
        prefix.append("000" + str(i))
    elif i < 1000:
        prefix.append("00" + str(i))
new_filenames = [prefix[i] + "_" + D_option + ".tiff" for i,filename in enumerate(all_files)]
for i, j in zip(all_files, new_filenames):
    os.rename(i, j)

