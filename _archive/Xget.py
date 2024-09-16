import importlib
import inspect

from rich.console import Console

console = Console()
# convert tests/mytest_class.py to tests.mytest_class

# dynamically import the module

test_class_dict = {}


def get_all_class_methods(module_path):

    module_name = module_path.replace("/", ".").replace(".py", "")
    # console.print(f"[dark_orange]Module: {module_name}[/]")
    mymodule = importlib.import_module(module_name)

    all_classes = []
    # get all class names
    for name in dir(mymodule):
        obj = getattr(mymodule, name)
        if inspect.isclass(obj):
            # print(name)
            all_classes.append(name)
    # Get the class from the module
    # class_name = "MyTestSample"  # Replace with the actual class name
    all_classes = [class_ for class_ in all_classes if class_.startswith("MyTest")]
    # console.print(f"Test Classes: {all_classes}")
    class_methods = []
    for class_name in all_classes:
        class_ = getattr(mymodule, class_name)

        # Find all class methods
        class_methods += [
            name
            for name in dir(class_)
            if callable(getattr(class_, name)) and name.startswith("my_test_")
        ]
        for method_name in class_methods:
            test_class_dict[method_name] = class_.__dict__[method_name]

    console.print("test class dict", test_class_dict)

    return class_methods


def get_all_classes(module_path):

    module_name = module_path.replace("/", ".").replace(".py", "")
    # console.print(f"[dark_orange]Module: {module_name}[/]")
    mymodule = importlib.import_module(module_name)

    all_classes = []
    # get all class names
    for name in dir(mymodule):
        obj = getattr(mymodule, name)
        if inspect.isclass(obj):
            # print(name)
            all_classes.append(name)
    # Get the class from the module
    # class_name = "MyTestSample"  # Replace with the actual class name
    all_classes = [class_ for class_ in all_classes if class_.startswith("MyTest")]
    # console.print(f"Test Classes: {all_classes}")

    return all_classes


if __name__ == "__main__":
    module_name = "tests/mytest_class.py"
    test_methods = get_all_class_methods(module_name)
    classes = get_all_classes(module_name)
    console.print("[green]Classes:[/]")
    for cls in classes:
        console.print(f"[cyan]{cls}[/]")
    console.print(f"[dark_orange]Number of test methods: {len(test_methods)}[/]")
    console.print("[green]Test Methods:[/]")
    for method in test_methods:
        console.print(f"\t[dark_orange]{method}[/]")
