from sys import argv
from time import time

def is_prime(n):
    factors = sum(n % i == 0 for i in range(2, n))
    return factors == 0

limit = int(argv[1])
t0 = time()
total = sum(1 for i in range(2, limit) if is_prime(i))
t1 = time()

print(total)
print(t1 - t0)
