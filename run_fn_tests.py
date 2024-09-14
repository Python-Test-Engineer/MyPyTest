import tests.mytest_fns as module_name
from rich.console import Console
from results import Results

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
    print(f"\nCalling function: {test_name}")
    try:
        console.print("[cyan]In try and running test...[/]")
        func()
        r.add_result(
            {
                "test_name": func.__name__,
                "test_result": "PASSED",
                "test_message": None,
            }
        )
    except Exception as e:
        r.add_result(
            {
                "test_name": func.__name__,
                "test_result": "FAILED",
                "test_message": str(e),
            }
        )
        print(e)
    finally:
        console.print("[cyan]In finally...[/]")
        console.print(r.get_results())
    # func()


console.print("[dark_orange]Test results[/]")
console.print(r.get_results())
console.print("[green]================ Test Summary ===================[/]")
r.get_result_totals()
console.print("[green]=================================================[/]")
