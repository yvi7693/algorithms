from datetime import date


def factorial(n: int) -> int:
    if not isinstance(n, int):  raise TypeError()
    if n < 0 or n > 20:  raise ValueError()

    result = 1

    for i in range(2, n+1):
        result *= i

    return result
# O(n) = 1 + (n + 1 - 2) * 1 = 1 + (n - 1) = n -> O(n)


def fibonacci(n: int) -> list[int]:
    if not isinstance(n, int):  raise TypeError()
    if n < 0: raise ValueError()
    if n == 0: return [0]

    results = [0, 1]

    i = 0

    while n >= (results[i] + results[i+1]):

        results.append(results[i] + results[i+1])

        i += 1

    return results
# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1) = 2 + 9n = n -> O(n)


def count_ones(n: int) -> int:
    if not isinstance(n, int):  raise TypeError()
    if n < 0:  raise ValueError()
    if n == 0: return 0

    result = []

    while n >= 1:
        result.append(n % 2)
        n //= 2

    result.reverse()

    str_result = ""

    for item in result:
        str_result += str(item)

    return int(str_result)
# O(n) = 1 + n * (1 + 1 + 1 + 1 + 1 + 1) + n + 1 + n = 2 + 6n + 2n = 2 + 8n = n -> O(n)


def is_palindrome(x: int) -> bool:
    if not isinstance(x, int):  raise TypeError()
    if x <= -2**31 or x >= 2**31 - 1:  raise ValueError()

    result = 0
    num = x

    while num > 0:

        result *= 10
        result += num % 10
        num //= 10

    return result == x
# O(n) = 1 + 1 + n * (1 + 1 + 1 + 1 + 1) = 2 + 5n = n -> O(n)

#   Problem:
# Разработать алгоритм определяющий какие дни недели и месяцы наиболее популярны по посещаемости сайта,
# и дни с наименьшей посещаемостью.
#
#   Output data:
# список с n - количеством, дней недель в формате номера дня недели (int), начиная с 0, отсортированный начиная от самого популярного по посещаемости
# список с n - количеством месяцев в формате номера месяца (int) отсортированный начиная от самого популярного по посещаемости
#
#   Input data:
# массив кортежей в формате дата (date), количество посещений(int)
# число int - количество вывода самых посещаемых дней и месяцев
#
#   Constrains:
# •Ограничение на память: 256MB
# •Ограничение на скорость: 2 секунды
# •Максимальное количество записей в данных: 10^5
#
#   Example:
# input:
# [(2023-01-04,100
# 2023-01-05,300
# 2023-01-06,180
# 2023-01-07,220
# 2023-01-08,170
# 2023-01-09,210
# 2023-01-10,160
# 2023-01-11,190
# 2023-01-12,230
# 2023-01-13,250)], 1
#
# output:
# [2]
# [1]

def top_attendance(data: list[tuple[date, int]], count: int) -> tuple[list[int],list[int]]:
    pass




