# Dependencies
- `pandas`

# Directory Structure
extensions.txt
- Lookup table for what file extensions to look for a given programming language that is being scanned for

readCodeBase.py
- Script that uses `extensions.txt` to read through a code base for a given set of extensions, and report its line count

project.gv
- Digraph of the project, showing structure, inputs, and outputs
- CLI are represented with colored circles

readCodeBase.gv
- Digraph of the code, showing flow
- CLI are represented with colored circles

test/
- Folder for testing and debugging various parts of the project