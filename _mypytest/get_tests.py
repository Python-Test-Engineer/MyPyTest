import importlib
import pathlib
from utils import display_test_result
from rich.console import Console
from results import Results
from utils import display_test_result

r = Results.get_instance()
console = Console()
location = pathlib.Path("./tests")

# .rglob() produces a generator too
all_test_files = list(location.glob("mytest_*.py"))
console.print(all_test_files)


for test_name in all_test_files:
    globals()[test_name] = importlib.import_module
    func = globals()[test_name]
    console.print(globals()[test_name])
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
