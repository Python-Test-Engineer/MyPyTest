# main.py
import os.path
import types
import sys
from rich.console import Console

console = Console()
# let's "import" module1 manually

# first we need to load the code from file
module_name = "module1"
module_file = "module1_source.py"
module_path = "."

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

# read source code from file
with open(module_rel_file_path, "r") as code_file:
    source_code = code_file.read()

# next we create a module object
module_name = types.ModuleType(module_name)
module_name.__file__ = module_abs_file_path

# insert a reference to the module in sys.modules
sys.modules[module_name] = module_name

# compile the module source code into a code object
# optionally we should tell the code object where the source came from
# the third parameter is used to indicate that our source consists of a sequence of statements
code = compile(source_code, filename=module_abs_file_path, mode="exec")
console.print(module_name.__dict__)
# execute the module
# we want the global variables to be stored in mod.__dict__
exec(code, module_name.__dict__)

# our module is now imported!
# We can use it directly via our mod variable

module_name.hello()
console.print(module_name.__dict__)
all_funcs = dir(module_name)
function_names = [func for func in all_funcs if func.startswith("my_test_")]
# console.print(function_names)

# # Dictionary to store function names as keys and functions as values
test_dict = {}

# # Populate the dictionary
for func_name in function_names:
    test_dict[func_name] = module_name.__dict__[func_name]

console.print("[dark_orange]Running fn tests...[/dark_orange]")

# # Now you can access and call the functions using the dictionary
for test_name, func in test_dict.items():
    console.print(f"[cyan]Test: {test_name}[/cyan]")
    try:
        func()
        result = {
            "test_name": func.__name__,
            "test_result": "PASSED",
            "test_message": None,
        }

    except Exception as e:
        result = {
            "test_name": func.__name__,
            "test_result": "FAILED",
            "test_message": str(e),
        }

        # print(e)
    finally:
        pass
