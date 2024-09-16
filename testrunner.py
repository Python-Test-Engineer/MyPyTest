import importlib

from tests.mytest_class import MyTestSample  # is src.add imported?

from rich.console import Console
from _mypytest.results import Results
from _mypytest.utils import display_test_result
from utils.read_mypytest import get_mytest_dir, get_mytest_files, get_version


cls_file = "tests.mytest_class"
mod = "tests.mytest_class"
MyTestSample = importlib.import_module(mod)
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

console.print("[dark_orange]================ RUN CLASS TESTS ===================[/]")
# console.print(globals())
all_objs = dir(MyTestSample)
method_names = [(str(obj)) for obj in all_objs if obj.startswith("my_test_")]
# console.print(method_names)
# # Dictionary to store function names as keys and functions as values

test_class_dict = {}

# # Populate the dictionary

for method_name in method_names:
    test_class_dict[method_name] = MyTestSample.__dict__[method_name]


# console.print("test class dict", test_class_dict)
console.print("[dark_orange]Running cls tests...[/dark_orange]")
for test_class_name, class_method in test_class_dict.items():
    console.print(f"[cyan]Test: {test_class_name}[/cyan]")
    try:
        class_method()
        result = {
            "test_name": test_class_name,
            "test_result": "PASSED",
            "test_message": None,
        }
        display_test_result(result, "PASSED")

        r.add_result(result)
    except Exception as e:
        result = {
            "test_name": test_class_name,
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

        # print(e)
    finally:
        pass


console.print("[green]================ Test Summary ===================[/]")
r.get_result_totals()
console.print("[green]=================================================[/]")
