import importlib
import inspect
from rich.console import Console
from _mypytest.utils import display_test_result
from utils.read_mypytest import get_mytest_dir, get_mytest_files, get_version
from _mypytest.header import do_header
from _mypytest.results import Results

r = Results.get_instance()
console = Console()


# HEADER
do_header()

# RUN TESTS
# Dynamically import the module
module_name = (
    "tests.mytest_mix"  # replace with the name of the module you want to import
)
module = importlib.import_module(module_name)

# CLASSES
# Get all classes in the module
classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

# Iterate over each class and invoke all its methods
for cls in classes:
    print("")
    console.print(f"[dark_orange bold]Class: {cls.__name__}[/]")
    methods = inspect.getmembers(cls, inspect.isfunction)
    methods = [method for method in methods if method[0].startswith("my_test")]
    for method_name, method in methods:
        console.print(f"[cyan]Test: {method_name}[/]")

# FN
console.print("\n[dark_orange]================ RUN FN TESTS ===================[/]")
mod = "tests.mytest_mix"
module_name = importlib.import_module(mod)

all_funcs = dir(module_name)
function_names = [func for func in all_funcs if func.startswith("my_test_")]
console.print(function_names)
