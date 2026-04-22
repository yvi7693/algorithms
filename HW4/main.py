from typing import Any


def bubble_sort(collection: list[Any], key = lambda obj: obj, order_by = lambda x, y: x > y) -> list[Any]:
    if not collection: return []

    length = len(collection)

    for i in range(1, length):
        for j in range(length-i):
            if not order_by(key(collection[j]), key(collection[j+1])):
                collection[j], collection[j+1] = collection[j+1], collection[j]

    return collection

# Лучший O(n^2)
# Средний O(n^2)
# Худший O(n^2)


def selection_sort(collection: list[Any],
                   key = lambda obj: obj,
                   order_by = lambda x, y: x > y) -> tuple[list[Any], int, int]:

    count_comparison = 0
    count_permutation = 0

    for i in range(len(collection) - 1):

        target = i

        for j in range(i + 1, len(collection)):

            count_permutation += 1
            if order_by(key(collection[j]), key(collection[target])):
                target = j

        collection[i], collection[target] = collection[target], collection[i]
        count_comparison += 1

    return collection, count_comparison, count_permutation

# Лучший O(n^2)
# Средний O(n^2)
# Худший O(n^2)


def recursive_sum(collection: list[int | float]) -> int | float:
    if not collection: return 0

    if len(collection) == 1: return collection[0]

    return collection[-1] + recursive_sum(collection[:-1])


def recursive_max(collection: list[int | float]) -> int | float:
    if not collection: return 0
    if len(collection) == 1: return collection[0]

    else:
        if recursive_max(collection[:-1]) > collection[-1]:

            return recursive_max(collection[:-1])

        else:
            return collection[-1]


def recursive_sum_even(collection: list[int | float]) -> int | float:
    if not collection: return 0

    if len(collection) == 1 and collection[0] % 2 == 0: return collection[0]

    else:
        if collection[-1] % 2 == 0:
            return recursive_sum_even(collection[:-1]) + collection[-1]

        else:
            return recursive_sum_even(collection[:-1])


def reverse_string(text: str) -> str:
    if not text: return ""

    if len(text) == 1: return text

    return text[-1] + reverse_string(text[:-1])


def is_palindrome(text: str) -> bool:

    if len(text) == 0:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])


def fibonacci(number: int) -> int:
    pass







