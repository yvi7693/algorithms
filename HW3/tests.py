import pytest

from HW3.main import max_in_range, rotate_and_reverse, reverse_even_numbers, add_one


@pytest.mark.parametrize(
    "collection, start, end, max, absolut_index, relative_index ", [
        ([1,2,3,4,5,6], 0, 2, 3, 2, 2),
        ([1, 1, 1, 1, 1], 1, 4, 1, 1, 0),
        ([6, 5, 4, 3 , 2, 1], 0, 4, 6, 0, 0),
        ([0, 0, 0, 0], 1, 2, 0, 1, 0),
        ([-1, -2, -2, -1], 1, 3, -1, 3, 2),
        ([4, 4, 8, 8], 1, 1, 4, 1, 0)
    ]
)
def test_max_in_range(collection, start, end, max, absolut_index, relative_index):
    assert max_in_range(collection, start, end) == (max, absolut_index, relative_index)


@pytest.mark.parametrize(
    "collection, k, expected", [
        ([1,2,3,4,5], 1, [4, 3, 2, 1 ,5]),
        ([1, 1, 1, 1], 3, [1, 1, 1, 1]),
        ([5, 4, 5, 4], 0, [5, 4, 5, 4]),
        ([1,2,3,4,5,6], 4, [2,1,6,5,4,3])
    ]
)
def test_rotate_and_reverse(collection, k, expected):
    assert rotate_and_reverse(collection, k) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ([1,2,3,4,5,6], [1,6,3,4,5,2]),
        ([1, 3, 5, 7], [1, 3, 5, 7]),
        ([2, 4, 6, 8], [8, 6, 4, 2]),
        ([0, 0, 5, 2, 2], [2, 2, 5, 0, 0])
    ]
)
def test_reverse_even_numbers(input, expected):
    assert reverse_even_numbers(input) == expected


@pytest.mark.parametrize(
    "input, expected", [
        ([1,2,3], [1,2,4]),
        ([9], [1, 0]),
        ([1, 9, 9, 9, 9], [2, 0, 0, 0 ,0]),
        ([9,9,9], [1, 0, 0, 0]),
    ]
)
def test_add_one(input, expected):
    assert add_one(input) == expected