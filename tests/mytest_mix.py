from src.app import add


def my_test_1001_add():
    actual_result = add(15, 20)
    expected_result = 35
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_1002_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_1003_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_1004_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_1005_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_1006_FAIL():
    actual_result = add(7, 2) + 10
    expected_result = 9
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_1007_FAIL():
    actual_result = add(17, 3) + 10
    expected_result = 20
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


class MyTestSample:
    # we can define setup and teardown methods as well

    def setup_method(self, method):
        print(f"\n[dark_orange italic]Running setup for {method.__name__}[/]")

    def teardown_method(self, method):

        print(f"\n[dark_orange italic]Running teardown for {method.__name__}[/]")

    def my_test_2001_cls_add_PASS():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2002_cls_add():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2003_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2004_cls_add_FAIL():
        actual_result = add(22, 2) + 10
        expected_result = 24
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"


class MyTestSample2:
    # we can define setup and teardown methods as well

    def my_test_2005_cls_add():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2006_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2007_cls_add_FAIL():
        actual_result = add(22, 2) + 10
        expected_result = 24
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"


class MyTestSample3:
    # we can define setup and teardown methods as well

    def my_test_2008_cls_add():
        actual_result = add(15, 20)
        expected_result = 35
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2009_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2010_cls_add_FAIL():
        actual_result = add(22, 2) + 10
        expected_result = 24
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2011_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"

    def my_test_2012_cls_add():
        actual_result = add(10, 30)
        expected_result = 40
        assert (
            actual_result == expected_result
        ), f"Actual result: {actual_result} - Expected result: {expected_result}"
