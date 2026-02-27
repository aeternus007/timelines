#!/usr/bin/env python3
import glob
from json import loads
from os import path, remove
from requests import get

base_path = path.split(__file__)[0]
version = glob.glob(path.join(base_path, "version_*"))[0].split("_")[-1]

response = get("https://raw.githubusercontent.com/aeternus007/timelines/refs/heads/main/files.json")
files = loads(response.text)
version_online = files[-1].split("_")[-1]

def filter_files(filename):
    if "json" in filename:
        return False
    if "update" in filename:
        return False
    
    return True

if version != version_online:
    for file in filter(filter_files, glob.glob(path.join(base_path, "**", "*"), recursive=True)):
        remove(file)
        print(f"{file} is deleted")

    for file in files:
        filename = path.join(base_path, path.split(file)[-1])
        print(f"{filename} is downloading")

        with open(filename, "w") as destination:
            destination.write(get(file).text)
            print(f"{destination} is done")