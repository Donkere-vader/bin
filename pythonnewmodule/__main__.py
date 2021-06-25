import sys
import os
import pathlib

print("Setting up new project...")

def to_camel_case(string) -> str:
    new_str = ""
    next_cap = True
    for let in string:
        if let == "_":
            next_cap = True
            continue
        
        new_str += let.upper() if next_cap else let.lower()
        next_cap = False

    return new_str


try:
    project_name = sys.argv[1]
except IndexError:
    print("Supply a project name ``pythonnew [NAME]``")
    exit()

print(f"Project name: {project_name}")

# mkdir
os.mkdir(project_name)
# cd
os.chdir(project_name)
# mkdir
os.mkdir(project_name)

print("Creating README...")
with open("README.md", 'w') as f:
    f.write(f"# {project_name}\n\nTODO\n")

print("Creating .gitignore...")
with open(".gitignore", 'wb') as f:
    git_ignore_content = open(f"{pathlib.Path(__file__).parent.absolute()}/gitignore_template", 'rb').read()
    f.write(git_ignore_content)

print("Creating python files...")
init_file = open(f"{project_name}/__init__.py", 'w')
init_file.write(f"from .{project_name} import {to_camel_case(project_name)}")
init_file.close()

main_file = open(f"{project_name}/{project_name}.py", 'w')
main_file.write(f"\n\nclass {to_camel_case(project_name)}:\n    def __init__(self):\n        pass")
main_file.close()

print("Initializing git repo...")
os.system("git init")

print("\nDone")
