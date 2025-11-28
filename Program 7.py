import time
import sys
var=1
start_time=time.time()

def is_harshad(n):
    # Calculate sum of digits
    digit_sum = 0
    temp = n
    while temp > 0:
        digit_sum += temp % 10
        temp //= 10
    
    # Check divisibility by digit sum
    return n % digit_sum == 0

n=int(input("Enter number:"))

end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))


