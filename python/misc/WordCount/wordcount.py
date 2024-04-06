'''
wordcount.py
Read in a directory, and recursively scan through it to run 

`pdftotext *.pdf - | tr -d '.' | wc -w`

on every .pdf file in the directory, then create a DataFrame with the name, location, and word count of the file  
'''
import pandas as pd
import sys
import os
import subprocess

'''
HELPER FUNCTIONS 
'''
def wordCount(path_to_file: str) -> int:
    w_c = 0
    # Run the bash command
    # path_to_file expected to point to a .pdf file
    output = subprocess.check_output("pdftotext " + path_to_file + " - | tr -d '.' | wc -w", shell=True)

    # Decode the output to string
    output_str = output.decode("utf-8")

    # Print the output
    w_c = output_str.strip()
    print("Number of words:", w_c)
    return w_c

def readCodeBase(root: str, ext_str: str, code_base_dict: dict) -> None:
    # Get a list of all relevant files, and sub-directories in root
    print(root)
    list_of_subdirs = next(os.walk(root))[1] # sub-directories
    print(list_of_subdirs)

    list_of_files = [file for file in next(os.walk(root))[2] if (len(file.split('.')) != 1) and (file.split('.')[1] == ext_str)] # files
    print(list_of_files)

    for file in list_of_files:
        line_count = wordCount(root + file)
        code_base_dict['file_name'].append(file)
        code_base_dict['path'].append(root) # This can be cleaned downstream
        code_base_dict['line_count'].append(line_count)

    for sub_dir in list_of_subdirs:
        readCodeBase(root + sub_dir + "/", ext_str, code_base_dict)

    return

'''
MAIN CODE
'''
path_to_code_base_root = sys.argv[1] # Absolute path

codebase_dict = {}
features = ['file_name', 'path', 'word_count']

for feature in features:
    codebase_dict[feature] = []

readCodeBase(path_to_code_base_root, '.pdf', codebase_dict)
codebase_df = pd.DataFrame(codebase_dict)

# need to calculate a name for the directory in which to put the reports
num_fwdslash = 0
for c in path_to_code_base_root:
    if c == '/': num_fwdslash += 1

root_components = path_to_code_base_root.split('/')
project_name = root_components[num_fwdslash-1]
print(project_name)

report_dir = './report_' + project_name
try: 
    os.mkdir(report_dir)
    print(f"Directory '{report_dir}' created successfully.")
except FileExistsError:
    print(f"Directory '{report_dir}' already exists.")
except Exception as e:
    print(f"An error occurred: {e}")

codebase_df.to_csv(report_dir + "/" + "report.csv")