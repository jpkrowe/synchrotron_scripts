#!/usr/bin/env python3
import os
from os.path import isfile, join
import sys


D_option = sys.argv[1]
all_files = [f for f in os.listdir(".") if isfile(join(".", f)) if f[-5:] == ".tiff" and f[0:4] == "i22-"]
file_ids = [i[4:10] for i in all_files]
new_filenames = [file_ids[i] + "_" + D_option + ".tiff" for i,filename in enumerate(all_files)]
for i, j in zip(all_files, new_filenames):
    os.rename(i, j)

