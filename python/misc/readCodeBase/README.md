# Dependencies
- `pandas`

# Overview
Recursive program that scans through an entire project for files with a specified set of extensions, and counts the number of lines in each file that it finds. 

The program constructs a dictionary out of this data, and uses pandas to compile a report out of this information.

Report details the name of the file, path to it, and the line count, for each file that is found. 

# Run Instructions
- `python3 readCodeBase.py path/to/project name_of_programming_language`
- Example: `python3 readCodeBase.py ~/someproject/ C`
    - This command would produce a directory named `report-someproject/`, and a file `report_C.csv` inside detailing the line count for each file ending with `.c`, `.h`, `.cpp`, `.hpp`, or `.cu` that is inside `~/someproject/`

# Future Work
Parallelize the scanning process over the different supported file extensions, (found in 'extensions.txt'). 

# Directory Structure
extensions.txt (DEP)
- Lookup table for what file extensions to look for a given programming language that is being scanned for

readCodeBase.py (FIN)
- Script that uses `extensions.txt` to read through a code base for a given set of extensions, and report its line count

project.gv (WIP)
- Digraph of the project, showing structure, inputs, and outputs
- CLI are represented with colored circles

readCodeBase.gv (WIP)
- Digraph of the code, showing flow
- CLI are represented with colored circles

test/ 
- Folder for testing and debugging various parts of the project