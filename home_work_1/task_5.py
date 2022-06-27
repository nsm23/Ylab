def count_find_num(primes: list, limit: int) -> list:
    primes_digit = 1
    for i in primes:
        primes_digit *= i
    step = limit // primes_digit
    count = 0
    max_n = 0
    for i in range(1, step + 1):
        x = i
        for j in primes:
            while x % j == 0:
                x //= j
        if x == 1:
            count +=1
            max_n = i * primes_digit
    if count == 0:
        return []
    return [count, max_n]
