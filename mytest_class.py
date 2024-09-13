import sys


from fns import add, mul, sub, div
from utils import color_result, store_result
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

    def my_test_cls_50(self):
        actual_result = add(5, 2)
        expected_result = 7
        print(f"Actual result: {actual_result} - Expected result: {expected_result}")
        color_result(actual_result, expected_result)
        store_result(sys._getframe().f_code.co_name, actual_result, expected_result)

    def my_test_cls_51(self):
        actual_result = add(10, 10)
        expected_result = 20
        print(f"Actual result: {actual_result} - Expected result: {expected_result}")
        color_result(actual_result, expected_result)
        store_result(sys._getframe().f_code.co_name, actual_result, expected_result)

    def my_test_cls_52(self):
        console.print("[green italic]MyTestSample.my_test_52[/]✅")
        assert add(1, 2) == 3

    def my_test_cls_53(self):
        console.print("[green italic]MyTestSample.my_test_53[/]✅")
        assert add(1, 2) == 3

    # def my_test_60_will_fail(self):
    #     """failing fn test in a class"""
    #     console.print("[red italic]Example of failed test[/]❌")
    #     assert add(1, 2) == 5


if __name__ == "__main__":
    t = MyTestSample()
    t.my_test_50()
