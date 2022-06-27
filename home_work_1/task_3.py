def zeros(data: int) -> int:
    factorial_digit = 1
    counter = 0
    if data == 0 or data == 1:
        return 0
    else:
        for i in range(1, data + 1):
            factorial_digit *= i
    while True:
        if factorial_digit % 10 == 0:
            counter += 1
            factorial_digit //= 10
        else:
            break
    return counter
    
#_____________________________________#
from math import prod


def zeros(rest: int) -> int:
    from math import prod
    counter = 0
    number = prod([i for i in range(1, rest + 1)])
    while True:
        if number % 10 == 0:
            counter += 1
            number //= 10
        else:
            break
    return counter
    
#______________________________________#
from functools import reduce


def zeros(rest: int) -> int:
    counter = 0
    number = reduce(lambda a, b: a * b, [i for i in range(1, rest + 1)])
    number = str(number)[:: -1]
    for i in number:
        if i == '0':
            counter += 1
        elif i != '0':
            break
    return counter
#_____________________________________#
from functools import reduce
from operator import mul


def zeros(data: int) -> int:
    counter = 0
    if data == 0:
        return counter
    num = reduce(mul, [i for i in range(1, data + 1)])
    while True:
        if num % 10 == 0:
            counter += 1
            num //= 10
        else:
            break
    return counter



