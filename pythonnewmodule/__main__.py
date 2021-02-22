import sys
import os
import pathlib

print("Setting up new project...")

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
open(f"{project_name}/__init__.py", 'w')
open(f"{project_name}/__main__.py", 'w')
open("__main__.py", 'w')

print("Initializing git repo...")
os.system("git init")

print("\nDone")