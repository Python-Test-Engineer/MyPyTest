from src.app import add


class MyTestSample:
    # we can define setup and teardown methods as well

    def setup_method(self, method):
        print(f"\n[dark_orange italic]Running setup for {method.__name__}[/]")

    def teardown_method(self, method):

        print(f"\n[dark_orange italic]Running teardown for {method.__name__}[/]")

    def my_test_2628_cls_add_FAIL():
        actual_result = add(15, 20) + 20
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2223_cls_add():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2224_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2625_cls_add_FAIL():
        actual_result = add(22, 2) + 10
        expected_result = 24
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"


class MyTestSample2:
    # we can define setup and teardown methods as well

    def my_test_301_cls_add():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_302_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_303_cls_add_FAIL():
        actual_result = add(22, 2) + 10
        expected_result = 24
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"
