from tests.mytest_class import MyTestSample
import tests.mytest_fns as module_name
from rich.console import Console
from _mypytest.results import Results
from _mypytest.utils import display_test_result

r = Results.get_instance()
console = Console()

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
