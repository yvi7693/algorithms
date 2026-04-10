

def factorial(n: int) -> int:
    if not isinstance(n, int):  raise TypeError()
    if n < 0 or n > 20:  raise ValueError()

    result = 1

    for i in range(2, n+1):
        result *= i

    return result


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


def count_ones(n: int) -> int:
    if not isinstance(n, int):  raise TypeError()
    if n < 0:  raise ValueError()

    result = []

    while n >= 1:
        result.append(n % 2)
        n //= 2

    result.reverse()

    str_result = ""

    for item in result:
        str_result += str(item)

    return int(str_result)


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






