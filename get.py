import importlib
import inspect

from rich.console import Console

console = Console()
# convert tests/mytest_class.py to tests.mytest_class

# dynamically import the module


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

        # console.print(f"class methods {class_methods}")

    return class_methods


if __name__ == "__main__":
    module_name = "tests/mytest_class.py"
    test_methods = get_all_class_methods(module_name)
    console.print(f"Test Methods: {test_methods}")
