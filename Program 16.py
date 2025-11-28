import time
import sys

var=1

start_time=time.time()

def aliquot_sum(n):
    1 is 0.
    if n <= 0:
        return 0

    # Initialize the sum of divisors
    total_sum = 0
    
    # Start checking for divisors from 1 up to n-1.
    # We will use a counter 'i' instead of the built-in range() function.
    i = 1
    
    # Iterate while the divisor candidate 'i' is less than n.
    while i < n:
        # Check if 'i' is a divisor of 'n' using the modulo operator (%)
        # We must avoid using any built-in functions like range or sum.
        if n % i == 0:
            # If 'i' divides 'n' evenly, it is a proper divisor.
            # Add it to the total sum.
            # Using basic arithmetic: total_sum = total_sum + i
            total_sum = total_sum + i
        
        # Manually increment the counter
        # Using basic arithmetic: i = i + 1
        i = i + 1
        
    return total_sum

n=int(input("Enter the number:"))
print(aliquot_sum(n))
end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
