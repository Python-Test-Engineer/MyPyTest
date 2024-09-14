import tests.mytest_fns as module_name
from rich.console import Console
from _mypytest.Result import Results

r = Results.get_instance()
console = Console()

all_funcs = dir(module_name)
function_names = [func for func in all_funcs if func.startswith("my_test_")]
console.print(function_names)


# # Dictionary to store function names as keys and functions as values
test_dict = {}


# # Populate the dictionary
for func_name in function_names:
    test_dict[func_name] = module_name.__dict__[func_name]


console.print("test dict", test_dict)

# # Now you can access and call the functions using the dictionary
for test_name, func in test_dict.items():
    console.print(f"\n[cyan]Test: {test_name}[/cyan]")
    try:
        func()
        result = {
            "test_name": func.__name__,
            "test_result": "PASSED",
            "test_message": None,
        }
        console.print("[green bold]PASSED ✅[/]")
        console.print(f"[green]{result}[/]")
        r.add_result(result)
    except Exception as e:
        result = {
            "test_name": func.__name__,
            "test_result": "FAILED",
            "test_message": str(e),
        }
        console.print("[red bold]FAILED ❌[/]")
        console.print(f"[red]{result}[/]")
        r.add_result(result)

        print(e)
    finally:
        pass


console.print("[green]================ Test Summary ===================[/]")
r.get_result_totals()
console.print("[green]=================================================[/]")
