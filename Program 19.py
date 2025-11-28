import time
import sys

var=1

start_time=time.time()
def count_divisors(n):
    
    if n <= 0:
        return 0
    
    # Special case: 1 has one divisor (itself)
    if n == 1:
        return 1

    divisor_count = 0
    i = 1 # Start checking divisors from 1
    
    # Iterate from 1 up to n
    while i <= n:
        # Check if 'i' divides 'n' evenly
        if n % i == 0:
            divisor_count = divisor_count + 1
        
        # Manually increment the counter
        i = i + 1
        
    return divisor_count

def is_highly_composite(n):
    
    if n <= 0:
        return False
    
    # 1 is defined as the first Highly Composite Number.
    if n == 1:
        return True
        
    # Calculate the number of divisors for the input 'n'
    n_divisors = count_divisors(n)
    
    # Start checking all numbers 'i' smaller than 'n'
    i = 1
    is_hcn = True
    
    # Iterate through all positive integers smaller than n
    while i < n:
        i_divisors = count_divisors(i)
        
        # If any smaller number 'i' has a divisor count greater than or equal to n's count,
        # then n is NOT highly composite.
        if i_divisors >= n_divisors:
            is_hcn = False
            # Exit the loop as soon as the condition is violated
            break
            
        # Manually increment the counter
        i = i + 1
        
    return is_hcn

n=int(input("Enter the number:"))
print(is_highly_composite(n))
end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
