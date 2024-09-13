from mytest_class import MyTestSample
from rich.console import Console
from results import Results

r = Results.get_instance()
console = Console()


all_objs = dir(MyTestSample)
method_names = [(str(obj)) for obj in all_objs if obj.startswith("my_test_")]
console.print(method_names)
# # Dictionary to store function names as keys and functions as values

test_class_dict = {}

# # Populate the dictionary

for method_name in method_names:
    test_class_dict[method_name] = MyTestSample.__dict__[method_name]


console.print("test class dict", test_class_dict)
# # Now you can access and call the functions using the dictionary

for test_class_name, method in test_class_dict.items():
    print(f"\nCalling function: {test_class_name}")
    # print(method)
    t = MyTestSample()
    t.my_test_50()
    t.my_test_51()
    t.my_test_52()


console.print("[dark_orange]Test results[/]")
console.print(r.get_results())
console.print("[green]================ Test Summary ===================[/]")
r.get_result_totals()
console.print("[green]=================================================[/]")
