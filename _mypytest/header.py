from utils.read_mypytest import get_mytest_dir, get_mytest_files, get_version
from rich.console import Console

console = Console()


def do_header():
    test_dir = get_mytest_dir()
    test_files = get_mytest_files()
    test_version = get_version()
    console.print("[dark_orange]================ HEADER ===================[/]")
    console.print(f"[cyan]Test dirctory: [green bold]{test_dir}[/][/cyan]")
    console.print(f"[cyan]Test files: [green bold]{test_files}[/][/cyan]")
    console.print(f"[cyan]Test version: [green bold]{test_version}[/][/cyan]")
    console.print("")
