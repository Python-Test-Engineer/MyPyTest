from src.app import add


def my_test_013_add():
    actual_result = add(15, 20)
    expected_result = 35
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_014_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_015_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_016_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_017_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_018_FAIL():
    actual_result = add(7, 2) + 10
    expected_result = 9
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_019_FAIL():
    actual_result = add(17, 3) + 10
    expected_result = 20
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"
