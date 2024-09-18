import functools
from rich.console import Console
from _mypytest.results import Results


def display_test_result(result={}, result_type="PASSED"):

    if result_type == "PASSED":
        console.print(f"[green]{result}[/]")
        console.print(f"[green bold]{result_type} ✅[/]")
        console.print("[cyan]END TEST[/cyan]")
        print("")
    if result_type == "FAILED":
        console.print(f"[red]{result}[/]")
        console.print(f"[red bold]{result_type} ❌[/]")
        console.print("[cyan]END TEST[/cyan]")
        print("")


r = Results.get_instance()
console = Console()


def color_result(actual_result, expected_result):
    if actual_result != expected_result:
        console.print("[red bold]FAILED ❌[/]")
    else:
        console.print("[green bold]PASSED ✅[/]")


def store_result(test_name, actual_result, expected_result, test_message=None):
    try:
        assert (
            actual_result == expected_result
        ), f"Actual result should be {expected_result}"
        r.add_result(
            {
                "test_name": test_name,
                "test_result": "PASSED",
                "test_message": test_message,
            }
        )
    except Exception as e:
        r.add_result(
            {"test_name": test_name, "test_result": "FAILED", "test_message": str(e)}
        )
        print(e)
        print("")


def store_test(func):

    @functools.wraps(func)
    def wrapper_store(*args, **kwargs):
        try:
            console.print("[cyan]In try and running test...[/]")
            func(*args, **kwargs)
            r.add_result(
                {
                    "test_name": func.__name__,
                    "test_result": "PASSED",
                    "test_message": None,
                }
            )
        except Exception as e:
            r.add_result(
                {
                    "test_name": func.__name__,
                    "test_result": "FAILED",
                    "test_message": str(e),
                }
            )
            print(e)
        finally:
            console.print("[cyan]In finally...[/]")
            console.print(r.get_results())

    return wrapper_store
