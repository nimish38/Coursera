import math

def prime_factors(n):
    factors = list()
    while n % 2 == 0:
        n = n//2
        factors.append(2)

    sqrt = math.floor(math.sqrt(n))
    i = 3
    while i <= sqrt:
        while n % i == 0:
            n = n // i
            factors.append(i)
        i += 2

    if n > 2:
        factors.append(n)
    return factors
