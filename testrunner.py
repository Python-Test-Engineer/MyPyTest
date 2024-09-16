import importlib
import inspect
from rich.console import Console
from _mypytest.utils import display_test_result
from utils.read_mypytest import get_mytest_dir, get_mytest_files, get_version

from _mypytest.results import Results

r = Results.get_instance()
console = Console()
test_dir = get_mytest_dir()
test_files = get_mytest_files()
test_version = get_version()
console.print("[dark_orange]================ HEADER ===================[/]")
console.print(f"[cyan]Test dirctory: [green bold]{test_dir}[/][/cyan]")
console.print(f"[cyan]Test files: [green bold]{test_files}[/][/cyan]")
console.print(f"[cyan]Test version: [green bold]{test_version}[/][/cyan]")
console.print("")
# Dynamically import the module
module_name = (
    "tests.mytest_class_01"  # replace with the name of the module you want to import
)
module = importlib.import_module(module_name)

# Get all classes in the module
classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

# Iterate over each class and invoke all its methods
for cls in classes:
    console.print(f"[dark_orange]Class: {cls.__name__}[/]")
    methods = inspect.getmembers(cls, inspect.isfunction)
    methods = [method for method in methods if method[0].startswith("my_test")]
    for method_name, method in methods:
        console.print(f"[cyan]Test: {method_name}[/]")
        try:
            # Create an instance of the class
            instance = cls()
            # Get the method as func without the instance
            func = getattr(cls, method_name)
            # Call the method without the instance
            func.__get__(None, cls)()
            result = {
                "test_name": method_name,
                "test_result": "PASSED",
                "test_message": None,
            }
            display_test_result(result, "PASSED")
            r.add_result(result)

        except Exception as e:
            result = {
                "test_name": method_name,
                "test_result": "FAILED",
                "test_message": str(e),
            }
            display_test_result(result, "FAILED")
            r.add_result(result)
            print(e)
        finally:
            pass

console.print("\n[dark_orange]================ RUN FN TESTS ===================[/]")
mod = "tests.mytest_fns"
module_name = importlib.import_module(mod)
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
        display_test_result(result, "PASSED")
        r.add_result(result)
    except Exception as e:
        result = {
            "test_name": func.__name__,
            "test_result": "FAILED",
            "test_message": str(e),
        }
        display_test_result(result, "FAILED")
        r.add_result(result)
        print(e)
    finally:
        pass

console.print("[green]================ Test Summary ===================[/]")
r.get_result_totals()
console.print("[green]=================================================[/]")
