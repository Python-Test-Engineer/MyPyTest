from src.app import add


def my_test_101_add():
    actual_result = add(15, 20)
    expected_result = 35
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_102_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_103_FAIL():
    actual_result = add(7, 2) + 10
    expected_result = 9
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"
