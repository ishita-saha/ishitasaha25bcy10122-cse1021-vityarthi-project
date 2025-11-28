#Write a function mean_of_digits(n) that returns the average
#of all digits in a number.

import time
import sys

def mean_of_digits(n: int) -> float:
    num = abs(n)

    if num == 0:
        return 0.0

    total_sum = 0
    count = 0
    while num > 0:
        digit = num % 10
        total_sum += digit
        count += 1
        num //= 10

    return total_sum / count

print("Welcome to the Digit Mean Calculator!")

try:
    user_input = input("Enter a whole number: ")
    number = int(user_input)
 
    start_time = time.time()
    result = mean_of_digits(number)
    end_time = time.time()
    
    print(f"\nThe number: {number}")
    print(f"The mean of the digits is: {result:.2f}")

    print("-" * 30)
    print(f"Execution Time: {end_time - start_time:.6f} seconds")

    print(f"Memory utilization: {sys.getsizeof(result)} bytes")

except ValueError:
    print("\nSorry, that wasn't a valid whole number. Please enter only digits.")
