from functools import reduce


def count_find_num(primesL: list, limit: int):
    if reduce(lambda x, y: x * y, primesL) > limit:
        return []
    result = []
    result.append(reduce(lambda x, y: x * y, primesL))
    for i in primesL:
        for j in result:
            j *= i
            while j <= limit and j not in result:
                result.append(j)
                j *= i
    return [len(result), max(result)]


#________________________________________________________#
from math import prod


def count_find_num(primesL: list, limit: int):
    all_digits = []
    total = prod(primesL)
    all_digits.append(total)
    if total > limit:
        return []

    for i in primesL:
        for total in all_digits:
            value = i * total
            if value <= limit and value not in all_digits:
                all_digits.append(value)
    return [len(all_digits), max(all_digits)]