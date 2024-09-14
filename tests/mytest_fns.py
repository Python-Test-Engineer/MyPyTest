from src.app import add


def my_test_10_add():
    actual_result = add(5, 2)
    expected_result = 7
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_20_add():
    actual_result = add(4, 2)
    expected_result = 6
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_30_FAIL():
    actual_result = add(4, 2) + 1
    expected_result = 6
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"
