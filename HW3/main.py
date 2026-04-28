from typing import Any


def max_in_range(collection: list[int | float], start: int, end: int, condition = True) -> tuple[int | float, int, int]:

    if not collection:  raise ValueError()
    if start > end:  raise ValueError()
    if len(collection) <= start or len(collection) <= end:  raise ValueError()

    max = 0
    continue_index = 0

    for i in range(start, end+1):
        if condition:
            max = collection[i]
            continue_index = i
            break

    absolut_index = continue_index

    for i in range(continue_index, end+1):
        if collection[i] > max and condition:
            max = collection[i]
            absolut_index = i
    relative_index = absolut_index - start

    return max, absolut_index, relative_index

# O(n) = 1 + 1 + n * (1 + 1 + 1) + 1 + n * (1 + 1 + 1) + 1 + 1 + 1 + 1 = 2 + 3n + 1 + 3n + 4 = 6n + 7 = n -> O(n)


def rotate_and_reverse(collection: list[Any], k: int) -> list[Any]:
    length = len(collection)
    if k == 0:  return collection

    iteration = 0

    while iteration != k:

        buff = collection[-1]

        for i in range(length-1, 0, -1):
            collection[i] = collection[i - 1]

        collection[0] = buff

        iteration += 1

    for i in range(length // 2):
        collection[i], collection[length - 1 - i] = collection[length - 1 - i], collection[i]

    return collection
# O(n) = 1 + 1 + 1 + n * (1 + 1 + 1 + 1 + 1 + n * (1 + 1 ) + 1 + 1 + 1 + 1) + n  * ( 1 + 1 + 1 + 1 + 1 ) = 3 + n * ( 9 + 2n) + 5n = 3 + 9n + 2n^2 + 5n = n^2 -> O(n^2)

def reverse_even_numbers(collection: list[int]) -> list[int]:
    indexes = []

    for i in range(len(collection)):
        if collection[i] % 2 == 0:
            indexes.append(i)

    for i in range(len(indexes) // 2):
        collection[indexes[i]], collection[indexes[len(indexes) - 1 - i]] = collection[indexes[len(indexes) - 1 - i]], collection[indexes[i]]

    return collection
# O(n) = 1 + n + n * (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) = 1 + n + 16n = n -> O(n)


def add_one(collection: list[int | float]) -> list[int | float]:
    if not collection:  raise ValueError()
    if collection[0] == 0:  raise ValueError()

    collection[-1] += 1

    for i in range(-1, -len(collection), -1):

        if collection[i] >= 10:

            collection[i - 1] += collection[i] // 10
            collection[i] = collection[i] % 10

    if collection[-len(collection)] >= 10:
        collection.append(collection[-len(collection)] % 10)
        collection[-len(collection)] = collection[-len(collection)] // 10

    return collection
# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 15 + 11n = n -> O(n)


def shift_right(collection: list[int | float]) -> list[int | float]:

    buff = collection[-1]

    for i in range(len(collection) - 1, 0, -1):
        collection[i] = collection[i - 1]

    collection[0] = buff

    return collection
# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1) + 1 + 1 = 4 + 3n = n -> O(n)


def shift_left(collection: list[int | float]) -> list[int | float]:
    buff = collection[0]

    for i in range(len(collection)-1):
        collection[i] = collection[i + 1]

    collection[-1] = buff

    return collection
# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1) + 1 + 1 = 4 + 4n = n -> O(n)


def binary_search(collection: list[Any], target: Any) -> int:

    length = len(collection)

    left = 0
    right = length - 1

    while left <= right:
        current_index = (left + right) // 2

        if target == collection[current_index]:
            return current_index

        if target < collection[current_index]:
            right = current_index - 1

        else:
            left = current_index + 1

    return -1

# O(n) = 1 + 1 + 1 + 1 + 1 + log n = log n -> O(log n)
