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
    print(prog_lang)
    with open('extensions.txt', 'r') as ext_file:
        for line in ext_file:
            if line.split('=')[0] == prog_lang:
                # print("Found {}".format(prog_lang))
                # extensions = line.split('=')[1]
                # print(extensions)
                pattern = re.compile("'.(.+?)'")
                matches = pattern.findall(line)
                # print(matches)
                # if matches:
                    # extensions = capture.group(1)
                    # print(extensions)
    return matches

# Reads a file, and returns how many lines there are 
def countLines(path_to_file: str) -> int:
    l_c = 0
    with open(path_to_file, 'r') as file:
        for line in file:
            l_c += 1
    return l_c

# Accepts a string representing the path to the codebase, an extension to scan for, and the dict in which to put the information 
# Recursive wrapper around the reading logic
def readCodeBase(root: str, ext_str: str, code_base_dict: dict) -> None:
    # Get a list of all relevant files, and sub-directories in root
    list_of_subdirs = next(os.walk(root))[1] # sub-directories
    print(list_of_subdirs)
    list_of_files = [file for file in next(os.walk(root))[2] if (len(file.split('.')) != 1) and (file.split('.')[1] == ext_str)] # files
    # list_of_files = next(os.walk(root))[2]
    print(list_of_files)

    for file in list_of_files:
        line_count = countLines(root + file)
        code_base_dict['file_name'].append(file)
        code_base_dict['path'].append(root) # This can be cleaned downstream
        code_base_dict['line_count'].append(line_count)
    
    print(code_base_dict)

    for sub_dir in list_of_subdirs:
        readCodeBase(root + sub_dir + "/", ext_str, code_base_dict)

    # for file in list_of_files:
    #     dot_split = file.split('.')
    #     if len(dot_split) == 1:
    #         continue
    #     print(file)
    #     print(file.split('.'))
    #     print(file.split('.')[0], file.split('.')[1])
        # file.delete()
    # TODO Add error-handling to `list_of_files`
    return

'''
MAIN CODE
# Program flow
# ext_list = readExtensions(prog_lang)
# code_base_dict = readCodeBase(path_to_root)
# pd.DataFrame(code_base_dict) 
'''
path_to_code_base_root = sys.argv[1] # Absolute path
prog_lang = sys.argv[2] # Performing multi scan is a feature for a later day

# print("Absolute path: {}".format(os.path.abspath(path_to_code_base_root)))
# print("Relative path: {}".format(path_to_code_base_root))

# TODO Add some error-handling around this
ext_list = readExtensions(prog_lang)
print(ext_list)

codebase_dict = {}
features = ['file_name', 'path', 'line_count']
for feature in features:
    codebase_dict[feature] = []

readCodeBase(path_to_code_base_root, ext_list[0], codebase_dict)
# print(codebase_dict)

# codebase_df = pd.DataFrame(codebase_dict)
# print(codebase_df)

