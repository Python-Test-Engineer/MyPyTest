import os
import importlib
import fnmatch
import pathlib
from rich.console import Console
from results import Results
from read_mypytest import get_mytest_dir, get_mytest_files, get_version

# main.py
import os.path
import types
import sys


r = Results.get_instance()
console = Console()
# get location of tests
test_dir = get_mytest_dir()
test_files = get_mytest_files()
test_version = get_version()

console.print("[dark_orange]================ HEADER ===================[/]")
console.print(f"[cyan]Test dirctory: [green bold]{test_dir}[/][/cyan]")
console.print(f"[cyan]Test files: [green bold]{test_files}[/][/cyan]")
console.print(f"[cyan]Test version: [green bold]{test_version}[/][/cyan]")
console.print("")

all_test_files = [
    f for f in os.listdir(test_dir) if os.path.isfile(os.path.join(test_dir, f))
]


all_test_files = [f for f in all_test_files if fnmatch.fnmatch(f, "mytest_*")]

console.print(all_test_files)

module_file = all_test_files[0]
console.print(module_file)


module_path = "./tests"

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, "r") as code_file:
    source_code = code_file.read()

# next we create a module object
mod = types.ModuleType(module_file)

console.print(mod)
console.print(dir(mod))