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

    def my_test_50_add(self):
        actual_result = add(5, 2)
        expected_result = 7
        print(f"Actual result: {actual_result} - Expected result: {expected_result}")
        color_result(actual_result, expected_result)
        store_result(sys._getframe().f_code.co_name, actual_result, expected_result)

    def my_test_51_add_fail(self):
        actual_result = add(10, 10) + 1
        expected_result = 20
        print(f"Actual result: {actual_result} - Expected result: {expected_result}")
        color_result(actual_result, expected_result)
        store_result(sys._getframe().f_code.co_name, actual_result, expected_result)

    def my_test_52_add(self):
        actual_result = add(22, 10)
        expected_result = 32
        print(f"Actual result: {actual_result} - Expected result: {expected_result}")
        color_result(actual_result, expected_result)
        store_result(sys._getframe().f_code.co_name, actual_result, expected_result)

    def my_test_53_add_fail(self):
        actual_result = add(25, 45) + 1
        expected_result = 70
        print(f"Actual result: {actual_result} - Expected result: {expected_result}")
        color_result(actual_result, expected_result)
        store_result(sys._getframe().f_code.co_name, actual_result, expected_result)
