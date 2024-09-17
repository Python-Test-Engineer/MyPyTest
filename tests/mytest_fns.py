from src.app import add


def my_test_fn_001_add():
    actual_result = add(15, 20)
    expected_result = 35
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_fn_002_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_fn_003_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_fn_004_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_fn_005_add():
    actual_result = add(8, 4)
    expected_result = 12
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_fn_006_FAIL():
    actual_result = add(7, 2) + 10
    expected_result = 9
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"


def my_test_fn_007_FAIL():
    actual_result = add(17, 3) + 10
    expected_result = 20
    assert (
        actual_result == expected_result
    ), f"Actual result: {actual_result} - Expected result: {expected_result}"
