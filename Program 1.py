#Write a function factorial(n) that calculates the factorial of
#a non-negative integer n (n!).

import time
import sys
var=1
def factorial(n):
    
    if n < 0:
        return "Factorial does not exist for negative numbers."
        start_time = time.time()
    else:
        fact = 1
        for i in range(1, n + 1):
            fact = fact*i
        return fact
num = int(input("Enter a number:"))
print(factorial(num))
end_time = time.time()
print("-" * 30)
print(f"Execution Time: {end_time - start_time:.6f} seconds")
print(f"Memory utilization:{sys.getsizeof(l1)} bytes")
