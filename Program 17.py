import time
import sys

var=1

start_time=time.time()
def aliquot_sum(n):
    """
    Calculates the sum of all proper divisors of a positive integer n (divisors less than n).
    This logic is implemented using only basic operators and a while loop, as required.
    """
    if n <= 0:
        return 0

    total_sum = 0
    i = 1 # Start checking for divisors from 1

    # Iterate up to n-1
    while i < n:
        # Check if 'i' is a divisor of 'n' using the modulo operator
        if n % i == 0:
            # Add it to the total sum
            total_sum = total_sum + i

        # Manually increment the counter
        i = i + 1

    return total_sum

def are_amicable(a, b):
    
    # 1. Amicable numbers must be different
    if a == b:
        return False
    
    # 2. Amicable numbers must be positive
    if a <= 0 or b <= 0:
        return False
        
    # Calculate the sum of proper divisors for 'a'
    sum_a = aliquot_sum(a)
    
    # Calculate the sum of proper divisors for 'b'
    sum_b = aliquot_sum(b)
    
    # Check the amicable condition: sum_a must equal b AND sum_b must equal a
    # The smallest amicable pair is (220, 284)
    is_amicable = (sum_a == b) and (sum_b == a)
    
    return is_amicable

n=int(input("Enter the number:"))
a=int(input("Enter the first number:"))
b=int(input("Enter the other number:"))
print(are_amicable(a, b))
end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
