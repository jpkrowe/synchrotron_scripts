import os
from os.path import isfile, join

for foldername in ["D11", "D12"]:
    all_files = [f for f in os.listdir(foldername) if isfile(join(foldername, f)) if f[-4:] == ".tif" and  f[:3] == foldername]
    new_filenames = [foldername + "/" + filename[3:-4] + "_" + foldername + ".tif" for filename in all_files]
    for i, j in zip(all_files, new_filenames):
        os.rename(foldername + "/" + i, j)

