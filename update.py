#!/usr/bin/env python3
import glob
from os import path, remove

def filter_files(filename):
    if "json" in filename:
        return False
    if "update" in filename:
        return False
    
    return True

base_path = path.split(__file__)[0]
for file in filter(filter_files, glob.glob(path.join(base_path, "**", "*"), recursive=True)):
    print(file)

    # remove(file)
