from _mypytest.read_mypytest import (
    get_version,
    get_mytest_dir,
    get_mytest_files,
    get_version,
    get_mytest_classes,
    get_mytest_funcs,
)
from rich.console import Console

console = Console()


def get_test_config():
    test_version = get_version()
    test_dir = get_mytest_dir()
    test_files = get_mytest_files()
    test_classes = get_mytest_classes()
    test_funcs = get_mytest_funcs()

    return (test_version, test_dir, test_files, test_classes, test_funcs)
