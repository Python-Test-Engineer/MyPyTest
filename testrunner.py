import importlib
import glob
import inspect
from rich.console import Console
from _mypytest.utils import display_test_result
from _mypytest.read_mypytest import get_mytest_dir, get_mytest_files, get_version
from _mypytest.header import do_header
from _mypytest.summary import do_summary_report
from _mypytest.discovery import get_test_config
from _mypytest.results import Results

r = Results.get_instance()
console = Console()


# HEADER
do_header()

# DISCOVER TESTS

(test_version, test_dir, test_files, test_classes, test_funcs) = get_test_config()
console.print(
    f"{test_version} - {test_dir} - {test_files}   - {test_classes} - {test_funcs}"
)


pattern = f"{test_dir}/**/{test_files}"
all_files = glob.glob(pattern, recursive=True)
all_modules = [f.replace("\\", ".").replace(".py", "") for f in all_files]
console.print(all_modules)
# RUN TESTS

# CLASSES
for mod in all_modules:
    module = importlib.import_module(mod)
    print(mod)
    classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

    # Iterate over each class and invoke all its methods
    for cls in classes:
        print("")
        console.print(f"[dark_orange bold]Class: {cls.__name__}[/]")
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
                console.print(f"[red italic]ERROR: {e}[/]")
            finally:
                pass
# FN
console.print("\n[dark_orange]================ RUN FN TESTS ===================[/]")
for mod in all_modules:

    module_name = importlib.import_module(mod)

    all_funcs = dir(module_name)
    function_names = [func for func in all_funcs if func.startswith("my_test_")]
    # console.print(function_names)

    # # Dictionary to store function names as keys and functions as values
    test_dict = {}

    # # Populate the dictionary
    for func_name in function_names:
        test_dict[func_name] = module_name.__dict__[func_name]

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
            console.print(f"[red italic]ERROR: {e}[/]")
        finally:
            pass

# SUMMARY REPORT

do_summary_report()
