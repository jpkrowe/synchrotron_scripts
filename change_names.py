import os
from os.path import isfile, join
import sys


D_option = sys.argv[1]
all_files = [f for f in os.listdir(".") if isfile(join(".", f)) if f[-5:] == ".tiff" and f[0:4] == "i22-"]
new_filenames = [filename[4:-5] + "_" + D_option + ".tiff" for filename in all_files]
for i, j in zip(all_files, new_filenames):
    os.rename(i, j)

