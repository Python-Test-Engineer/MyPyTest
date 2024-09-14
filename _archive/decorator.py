import functools
from rich.console import Console
from results import Results

from src.app import add

r = Results.get_instance()
console = Console()


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


@store_test
def my_test_10_add():
    actual_result = add(5, 2)
    expected_result = 7
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


@store_test
def my_test_20_add():
    actual_result = add(4, 2)
    expected_result = 6

    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


@store_test
def my_test_30_FAIL():
    actual_result = add(4, 2) + 1
    expected_result = 6

    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


if __name__ == "__main__":

    my_test_10_add()
    my_test_20_add()
    my_test_30_FAIL()
    console.print("[green]================ Test Summary ===================[/]")
    r.get_result_totals()
    console.print("[green]=================================================[/]")
