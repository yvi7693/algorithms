
import pytest

from HW4.main import bubble_sort, selection_sort, recursive_sum, recursive_max, recursive_sum_even, reverse_string, \
    is_palindrome


@pytest.mark.parametrize(
    "collection, order_by, expected", [
        ([1,2,3,4,5], lambda x,y: x > y, [5,4,3,2,1]),
        ([5,4,3,2,1], lambda x,y: x < y, [1,2,3,4,5]),
        ([-2, -1, -3, -4], lambda x,y: x > y, [-1, -2, -3, -4]),
        ([1, 1, 2, 2, 3, 3], lambda x,y: x >= y, [3, 3, 2, 2, 1, 1]),
        ([1], lambda x,y: x >= y, [1]),
        ([1, 2], lambda x,y: x > y, [2, 1]),
        ([], lambda x,y: x > y, [])

    ]
)
def test_bubble_sort_positive_and_boundary(collection, order_by, expected):
    assert bubble_sort(collection, order_by=order_by) == expected


@pytest.mark.parametrize(
    "collection, order_by, expected", [
        ([1, 2, 3, 4, 5], lambda x, y: x > y, ([5, 4, 3, 2, 1], 4, 10)),
        ([5, 4, 3, 2, 1], lambda x, y: x < y, ([1, 2, 3, 4, 5], 4 , 10)),
        ([-2, -1, -3, -4], lambda x, y: x > y, ([-1, -2, -3, -4], 3, 6)),
        ([1, 1, 2, 2, 3, 3], lambda x, y: x >= y, ([3, 3, 2, 2, 1, 1], 5, 15)),
        ([1], lambda x, y: x >= y, ([1], 0, 0)),
        ([1, 2], lambda x, y: x > y, ([2, 1], 1, 1)),
        ([], lambda x, y: x > y, ([], 0, 0))

    ]
)
def test_selection_sort_positive_and_boundary(collection, order_by, expected):
    assert selection_sort(collection, order_by=order_by) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ([1,2,3,4,5], 15),
        ([1], 1),
        ([-1, -2, -3], -6),
        ([0,0,0,1], 1)
    ]
)
def test_recursive_sum_positive_and_boundary(input, expected):
    assert recursive_sum(input) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ([1,2,3,4,5], 5),
        ([1], 1),
        ([-1, -2, -3], -1),
        ([0,0,0,1], 1),
        ([1,1,1,1], 1),
    ]
)
def test_recursive_max_positive_and_boundary(input, expected):
    assert recursive_max(input) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ([1,2,3,4,5], 6),
        ([1], 0),
        ([-1, -2, -3], -2),
        ([0,0,0,1], 0),
        ([2,4,6,8], 20)
    ]
)
def test_recursive_sum_even_positive_and_boundary(input, expected):
    assert recursive_sum_even(input) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ("hello", "olleh"),
        ("", ""),
        ("H", "H"),
        ("yaroslav volkov", "voklov valsoray")
    ]
)
def test_reverse_string_positive_and_boundary(input, expected):
    assert reverse_string(input) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ("hello", False),
        ("", True),
        ("H", True),
        ("yaroslav volkov", False),
        ("город дорог", True),
        ("как", True)
    ]
)
def test_is_palindrome_positive_and_boundary(input, expected):
    assert is_palindrome(input) == expected


