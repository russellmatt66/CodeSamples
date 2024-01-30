import sys 
import os
import pandas as pd 
import re

# import threading
# import concurrent.futures
'''
HELPER FUNCTIONS
'''
# Accepts a string representing the language to scan the code-base for
# Returns a list of the file extensions to look for
def readExtensions(prog_lang: str) -> list[str]:
    with open('extensions.txt', 'r') as ext_file:
        for line in ext_file:
            if line[0] == prog_lang:
                # print("Found {}".format(prog_lang))
                # extensions = line.split('=')[1]
                # print(extensions)
                pattern = re.compile("'(.+?)'")
                matches = pattern.findall(line)
                print(matches)
                # if matches:
                    # extensions = capture.group(1)
                    # print(extensions)
    return matches

# Reads the lines of a file, and places the file name into a dict along with how many there are 
def readFile(path_to_file: str) -> dict[str,int]:
    return {}

# Accepts a string representing the path to the codebase, and a list of extensions to scan for 
# Wrapper around the reading logic
def readCodeBase(path_to_code_base_root: str, ext_list: list[str]) -> dict[str, int]:
    return {}

'''
MAIN CODE
'''
path_to_code_base_root = sys.argv[1] # Absolute path
prog_lang = sys.argv[2] # Performing multi scan is a feature for a later day

# print("Absolute path: {}".format(os.path.abspath(path_to_code_base_root)))
# print("Relative path: {}".format(path_to_code_base_root))

ext_list = readExtensions(prog_lang)
print(ext_list)
# Program flow
# ext_list = readExtensions(prog_lang)
# code_base_dict = readCodeBase(path_to_root)
# pd.DataFrame(code_base_dict) 