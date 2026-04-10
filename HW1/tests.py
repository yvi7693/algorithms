import pytest

from HW1.main import even_sum, most_common, two_sum


@pytest.mark.parametrize(
    "input,expected", [
        ([1,2,3,4,5,6], 12),
        ([-1, -2, -3, -4, -5, -6], 1),
        ([2, 4, 6, 8], 20),
        ([], 0),
        ([1, 3, 5, 7], 0),
        ([0, 0, 0, 0], 0),
        ([2, 2, 2, 2], 8),
        ([3, 3, 3, 3], 0),
        ([-1, -1, -1, -1], 0),
        ([-2, 2, -4, 4], 0),
        ([-2, -2, 4, 4, 1, -3], 4),
        ([7], 0),
        ([6], 6)

    ]
)
def test_even_sum_different_value(input, expected):
    assert even_sum(input) == expected


def test_even_sum_incorrect_type():
    with pytest.raises(TypeError):
        even_sum("")


def test_even_sum_incorrect_type_item():
    with pytest.raises(TypeError):
        even_sum([""])


def test_even_sum_incorrect_value_positive():
    with pytest.raises(ValueError):
        even_sum([2 * 10**5, 2 * 10**6])


def test_even_sum_incorrect_value_negative():
    with pytest.raises(ValueError):
        even_sum([-2 * 10**5, -2 * 10**6])



@pytest.mark.parametrize(
    "input, expected", [
        ([1,2,2,3,3,3,4,4,4,4], 4),
        ([1,2,3,4,5], 1),
        ([1], 1),
        ([1, 1, 1, 1], 1),
        ([-1, -2, -3, -4], -4),
        ([-2, -2, -2, -3], -2),
        ([-1, 0, 1], -1),
        ([-1], -1),
        ([1, 1, 1, 2, 2, 2], 1),
        ([-2, -2, -2, -1, -1 , -1], -2),
        ([0, 0, 0], 0)

    ]
)
def test_most_common_different_value(input, expected):
    assert most_common(input) == expected


def test_most_common_incorrect_value_positive():
    with pytest.raises(ValueError):
        most_common([2 * 10**5, 2 * 10**6])


def test_most_common_incorrect_value_negative():
    with pytest.raises(ValueError):
        most_common([-2 * 10**5, -2 * 10**6])


def test_most_common_incorrect_type_array():
    with pytest.raises(TypeError):
        most_common("")


def test_most_common_incorrect_type_item():
    with pytest.raises(TypeError):
        most_common([""])


def test_two_sum_incorrect_type_array():
    with pytest.raises(TypeError):
        two_sum("", 1)


def test_two_sum_incorrect_type_item():
    with pytest.raises(TypeError):
        two_sum(["", "", ""], 1)


def test_two_sum_incorrect_type_target():
    with pytest.raises(TypeError):
        two_sum([1, 2, 3], "")


def test_two_sum_incorrect_length_array():
    with pytest.raises(ValueError):
        two_sum([1], 2)


def test_two_sum_incorrect_value_array():
    with pytest.raises(ValueError):
        two_sum([-111, -200, 200, 300], 2)


def test_two_sum_incorrect_value_target():
    with pytest.raises(ValueError):
        two_sum([1,2,3], 200)


@pytest.mark.parametrize(
    "array, target, expected", [
        ([2,7,11,15], 9, [0,1]),
        ([3,2,4], 6, [1,2]),
        ([3, 4, 6], 5, []),
        ([-1, -2, -4], -3, [0,1]),
        ([0, 0, 0], 0, [0,1]),
        ([1, 2, 3, 4], 5, [0,3]),
        ([0, 1, 2 ,3], 2, [0,2]),
        ([-1,-2,-3], -6, []),
        ([0,2,3,1], 3, [0,2])

    ]
)
def test_two_sum_incorrect_length_array(array, target, expected):
    assert two_sum(array, target) == expected




