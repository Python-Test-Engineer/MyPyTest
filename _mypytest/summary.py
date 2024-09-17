from utils.read_mypytest import get_mytest_dir, get_mytest_files, get_version
from rich.console import Console
from _mypytest.results import Results

console = Console()

r = Results.get_instance()


def do_summary_report():
    console.print("")
    console.print("[green]================ Test Summary ===================[/]")
    r.get_result_totals()
    console.print("[green]=================================================[/]")
