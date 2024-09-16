import importlib
import pathlib
from rich.console import Console
from results import Results


r = Results.get_instance()
console = Console()
location = pathlib.Path("./tests")


all_test_files = list(location.glob("mytest_*.py"))
console.print(all_test_files)

# run tests
for test_file in all_test_files:
    # globals()[test_file] = importlib.import_module(test_file)
    console.print("The module names are :", test_file)

console.print("Now import these modules...get fns...run them...save results")
