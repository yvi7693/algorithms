import pytest

from HW2.main import factorial, fibonacci, count_ones, is_palindrome


@pytest.mark.parametrize(
    "input, expected", [
        (3, 6),
        (1, 1),
        (0, 1),
        (2, 2)
    ]
)
def test_factorial_different_value(input, expected):
    assert factorial(input) == expected


def test_factorial_incorrect_type():
    with pytest.raises(TypeError):
        factorial("")


def test_factorial_incorrect_value():
    with pytest.raises(ValueError):
        factorial(100)


def test_factorial_negative_value():
    with pytest.raises(ValueError):
        factorial(-5)


@pytest.mark.parametrize(
    "input, expected", [
        (0, [0]),
        (5, [0, 1, 1, 2, 3, 5]),
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2])
    ]
)
def test_fibonacci_different_values(input, expected):
    assert fibonacci(input) == expected


def test_fibonacci_incorrect_type():
    with pytest.raises(TypeError):
        fibonacci("")


def test_fibonacci_incorrect_value():
    with pytest.raises(ValueError):
        fibonacci(-2)


@pytest.mark.parametrize(
    "input, expected", [
        (0, 0),
        (1, 1),
        (2, 10),
        (42, 101010),
        (43, 101011)
    ]
)
def test_count_ones(input, expected):
    assert count_ones(input) == expected


def test_count_ones_incorrect_type():
    with pytest.raises(TypeError):
        count_ones('')


def test_count_ones_negative_values():
    with pytest.raises(ValueError):
        count_ones(-5)

@pytest.mark.parametrize(
    "input, expected", [
        (121, True),
        (11, True),
        (1, True),
        (0, True),
        (5555555, True),
        (1234554321, True),
        (123, False),
        (10, False),
        (-121, False),
        (-1, False)
    ]
)
def test_is_palindrome(input, expected):
    assert is_palindrome(input) == expected


def test_is_palindrome_incorrect_type():
    with pytest.raises(TypeError):
        is_palindrome("")


def test_is_palindrome_incorrect_value():
    with pytest.raises(ValueError):
        is_palindrome(2**31)
