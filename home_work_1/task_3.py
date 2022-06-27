import math
import re


def zeros(n):
    zero_str = str(math.factorial(n))
    counter = len(''.join(re.findall(r"[0]+$", zero_str)))

    return counter


def zeros(n):
    counter = 0
    if n == 0 or n == 1:
        return counter
    else:
        while n > 1:
            n = n // 5
            counter += n
        return counter

