import os

# Wrapper around os.mkdir + exception handling + adds README.md
def createDir(path_to_dir: str) -> None:
    try:
        os.mkdir(path_to_dir)
        print(f"Directory '{path_to_dir}' created successfully")
    except FileExistsError:
        print(f"Directory '{path_to_dir}' already exists")
    except Exception as e: 
        print(f"An error occurred: {e}")
    
    with open(path_to_dir + 'README.md', 'w') as readme:
        readme.write('# WIP')
    return

# Who cares about this being all the same spaghetti?
# It makes the individual languages amenable to customization in the future w/out a serious refactor
def templateC(path_to_root: str) -> None:
    createDir(path_to_root)
    dir_names = ['include/', 'src/', 'test/', 'data/', 'benchmarking/', 'debug/', 'build/']
    for dir in dir_names:
        createDir(path_to_root + dir)
    return

def templateCpp(path_to_root: str) -> None:
    createDir(path_to_root)
    dir_names = ['include/', 'src/', 'test/', 'data/', 'benchmarking/', 'debug/', 'build/']
    for dir in dir_names:
        createDir(path_to_root + dir)
    return

def templatePython(path_to_root: str) -> None:
    createDir(path_to_root)
    dir_names = ['include/', 'src/', 'test/', 'data/', 'benchmarking/', 'debug/', 'build/']
    for dir in dir_names:
        createDir(path_to_root + dir)
    return

def templateCUDA(path_to_root: str) -> None:
    createDir(path_to_root)
    dir_names = ['include/', 'src/', 'test/', 'data/', 'machine-learning/', 'debug/', 'build/']
    for dir in dir_names:
        createDir(path_to_root + dir)
    return