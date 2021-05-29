import math
from functools import reduce

def primeWrt(n: int, primes: list) -> bool:
    for p in primes:
        if n % p == 0:
            return False
        else:
            continue
    return True

def isPrime(n: int) -> bool:
    if n <= 3:
        return True
    else:
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                return False
            else: continue
    return True

def primesLessThan(n: int) -> list:
    return filter(isPrime, range(2, n + 1))

def primeLogs(n: int) -> list:
    primes = primesLessThan(n)
    res = map((lambda x: int(math.log(n, x))), primes)
    return res

def prod(l: list) -> int:
    return reduce((lambda x, y: x * y), l)

def primeFactors(n: int) -> list:
    primes = primesLessThan(n)
    res = []
    for p in primes:
        lgbn = int(math.log(n, p))
        ps = [p] * lgbn
        res.extend(ps)
    return res

def evenlyDivisible(n: int) -> int:
    return prod(primeFactors(n))

def outList(l: list):
    for j in l: print(j)

l1p: list = primesLessThan(10)
l2p: list = primesLessThan(20)

outList(l1p)
outList(l2p)
