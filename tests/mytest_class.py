import sys


from src.app import add
from _mypytest.utils import color_result, store_result
from rich.console import Console

from results import Results

r = Results.get_instance()
console = Console()


class MyTestSample:
    # we can define setup and teardown methods as well

    def setup_method(self, method):
        console.print(f"\n[dark_orange italic]Running setup for {method.__name__}[/]")

    def teardown_method(self, method):

        console.print(
            f"\n[dark_orange italic]Running teardown for {method.__name__}[/]"
        )

    def my_test_201_cls_add():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_202_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_203_cls_FAIL():
        actual_result = add(22, 2) + 10
        expected_result = 24
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"
