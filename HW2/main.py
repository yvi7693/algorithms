
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


