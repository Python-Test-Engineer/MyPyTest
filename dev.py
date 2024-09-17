import importlib
import inspect
from rich.console import Console
from _mypytest.utils import display_test_result
from utils.read_mypytest import get_mytest_dir, get_mytest_files, get_version
from _mypytest.header import do_header
from _mypytest.discovery import get_test_config
from _mypytest.results import Results

r = Results.get_instance()
console = Console()


# HEADER
do_header()

test_discovery = get_test_config()
console.print(test_discovery)
