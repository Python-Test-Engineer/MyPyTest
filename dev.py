import importlib
import inspect

# Dynamically import the module
module_name = "tests.mytest_class_01"  # replace with your module name
module = importlib.import_module(module_name)

# Get all classes in the module
classes = [cls for cls in module.__dict__.values() if inspect.isclass(cls)]

# Iterate over each class and invoke its methods
for cls in classes:
    instance = cls()  # create an instance of the class
    methods = [
        method
        for method in dir(instance)
        if callable(getattr(instance, method))
        and not method.startswith("__")
        and method.startswith("my_test_")
    ]
    print(f"Class: {cls.__name__}")
    print(methods)
    for method in methods:
        print(f"Invoking method: {method}")
        # # getattr(instance, method)()  # invoke the method
        # cls.method.__name__()

print(dir(module.__dict__))
