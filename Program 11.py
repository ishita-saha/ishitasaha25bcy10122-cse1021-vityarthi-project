import time
import sys
import math

def distinct_prime_factors(n):
    factors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            factors.add(i)
            n //= i
        i += 1
    if n > 1:
        factors.add(n)
    return factors

number = int(input("Enter a number: "))

start_time = time.time()
factors = distinct_prime_factors(number)
end_time = time.time()

print(f"\nThe number {number} has {len(factors)} distinct prime factors: {factors}")
print(f"Execution time: {end_time - start_time:.6f} seconds")
print(f"Memory utilization: {sys.getsizeof(factors)} bytes")
