#!/usr/bin/env python3
import glob
from os import path, remove
import re
from requests import get

from bs4 import BeautifulSoup as bs

base_url = "https://github.com/aeternus007/timelines/"
sub_url = base_url + "https://github.com/aeternus007/timelines/tree/main/src"

base_raw_url = "https://raw.githubusercontent.com/aeternus007/timelines/refs/heads/main/"
sub_raw_url = base_raw_url + "src/"

version_pattern = re.compile(r"version_[0-9]+\.[0-9]*")
file_pattern = re.compile(r"[a-zA-z0-9]+\.[a-zA-z0-9]+")

page = get(sub_url, headers= {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0}"})
print(page)
print(page.text)
# [filename.extract().get_text() for filename in bs(get(base_url).text, "lxml").find_all(title=file_pattern)] + ["src" + filename.extract().get_text() for filename in bs(get(sub_url).text, "lxml").find_all(title=file_pattern)]
filenames = bs(page.text, "lxml").find_all(title=file_pattern)
print(filenames)

# def check_for_new():
#     return

# def get_file_urls():
#     return

# def filter_files(filename):
#     if "json" in filename:
#         return False
#     if "update" in filename:
#         return False
    
#     return True

# base_path = path.split(__file__)[0]
# for file in filter(filter_files, glob.glob(path.join(base_path, "**", "*"), recursive=True)):
#     print(file)

#     # remove(file)
