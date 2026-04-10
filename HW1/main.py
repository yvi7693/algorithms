

def even_sum(array: list[int]) -> int:
    if not isinstance(array, list): raise TypeError("Тип данных не list")

    for i in range(len(array)):
        if array[i] > 2 * 10**4 or array[i] < -2 * 10**4:
            raise ValueError("Не допустимый диапазон значений")

    if not array: return 0

    summa = sum([array[i] for i in range(len(array)) if array[i] % 2 == 0])

    if summa < 0: return 1

    return summa

def most_common(array: list[int]) -> int:
    if not isinstance(array, list):  raise TypeError("Тип данных не list")

    for i in range(len(array)):
        if array[i] > 2 * 10**4 or array[i] < -2 * 10**4:
            raise ValueError("Не допустимый диапазон значений")

    max_count = 0
    search_index = 0

    for i in range(len(array)):

        count = 0

        for j in range(len(array)):
            if array[i] == array[j]:
                count += 1

        if count > max_count:
            max_count = count
            search_index = i

        elif count == max_count:
            if array[i] < array[search_index]:
                search_index = i

    return array[search_index]


def two_sum(array: list[int], target: int) -> list[int]:
    if not isinstance(array, list):  raise TypeError()
    if not isinstance(target, int):  raise TypeError()

    if len(array) <= 2 or len(array) >= 104:  raise ValueError()
    if target <= -109 or target >= 109:  raise ValueError()

    for item in array:
        if item <= -109 or item >= 109:  raise ValueError()

    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i, j]

    return []







