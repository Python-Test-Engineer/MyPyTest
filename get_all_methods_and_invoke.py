import importlib
import inspect
from rich.console import Console

console = Console()

# Dynamically import the module
module_name = (
    "tests.mytest_class_01"  # replace with the name of the module you want to import
)
module = importlib.import_module(module_name)

# Get all classes in the module
classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

# Iterate over each class and invoke all its methods
for cls in classes:
    console.print(f"[dark_orange]Class: {cls.__name__}[/]")
    methods = inspect.getmembers(cls, inspect.isfunction)
    methods = [method for method in methods if method[0].startswith("my_test")]
    for method_name, method in methods:
        console.print(f"[cyan]Test: {method_name}[/]")
        try:
            # Create an instance of the class
            instance = cls()
            # Get the method without the instance
            method = getattr(cls, method_name)
            # Call the method without the instance
            method.__get__(None, cls)()
            console.print("[green bold]PASSED ✅[/]")
            print("")
        except Exception as e:
            console.print("[red]FAILED ❌[/]")
            console.print(f"[red]Error calling method: {e}[/]")
            print("")
