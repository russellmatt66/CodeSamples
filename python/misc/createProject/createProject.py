import sys
import projectTemplates

project_root = sys.argv[1]
prog_lang = sys.argv[2]

print((project_root, type(project_root)))
print((prog_lang, type(prog_lang)))

print(prog_lang.lower())
# Can always implement other languages later on 
if prog_lang.lower() != 'cpp' and prog_lang.lower() != 'c' and prog_lang.lower() != 'python' and prog_lang.lower() != 'cuda':
    print("Please provide the second argument as either {}, {}, {}, or {}".format('c','cpp','python','cuda'))

# Python doesn't have native 'switch' statement
if prog_lang.lower() == 'c':
    projectTemplates.templateC(project_root)
elif prog_lang.lower() == 'cpp':
    projectTemplates.templateCpp(project_root)
elif prog_lang.lower() == 'python': 
    projectTemplates.templatePython(project_root)
elif prog_lang.lower() == 'cuda':
    projectTemplates.templateCUDA(project_root)