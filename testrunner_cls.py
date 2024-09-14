from tests.mytest_class import MyTestSample
from rich.console import Console
from _mypytest.results import Results

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


console.print("test class dict", test_class_dict)
# Now you can access and call the functions using the dictionary

# Now you can access and call the functions using the dictionary
for test_class_name, class_method in test_class_dict.items():
    # print(self)
    try:
        class_method()
        result = {
            "test_name": test_class_name,
            "test_result": "PASSED",
            "test_message": None,
        }
        console.print("[green bold]PASSED ✅[/]")
        console.print(f"[green]{result}[/]")
        r.add_result(result)
    except Exception as e:
        result = {
            "test_name": test_class_name,
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
