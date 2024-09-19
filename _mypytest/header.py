from _mypytest.read_mypytest import (
    get_mytest_dir,
    get_mytest_files,
    get_version,
    get_mytest_classes,
    get_mytest_funcs,
)
from rich.console import Console

console = Console()


def do_header():
    test_dir = get_mytest_dir()
    test_files = get_mytest_files()
    test_version = get_version()
    test_classes = get_mytest_classes()
    test_funcs = get_mytest_funcs()
    console.print("[dark_orange]================ HEADER ===================[/]")
    console.print(f"[cyan]Test version: [green bold]{test_version}[/][/cyan]")
    console.print(f"[cyan]Test dirctory: [green bold]{test_dir}[/][/cyan]")
    console.print(f"[cyan]Test files: [green bold]{test_files}[/][/cyan]")
    console.print(f"[cyan]Test classes: [green bold]{test_classes}[/][/cyan]")
    console.print(f"[cyan]Test funcs: [green bold]{test_funcs}[/][/cyan]")
    console.print("")
