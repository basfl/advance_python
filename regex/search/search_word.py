import re
import os.path
import sys
"""
set the path to this current directory
"""
module_path = "./search"
module_file = ""
path = os.path.join(module_path, module_file)
abs_path = os.path.abspath(path)
sys.path.append(abs_path)


def lookup_word(fn):
    # print(abs_path+"\\"+fn)
    file_path = abs_path+"\\"+fn
    with open(file_path) as f:
        lines = f.readlines()
    lineNum = 0
    for line in lines:
        line.strip("\n\r")
        lineNum += 1
        searchResult = re.search("main", line, re.M | re.I)
        if searchResult:
            print(f'{str(lineNum)} : {line}')
