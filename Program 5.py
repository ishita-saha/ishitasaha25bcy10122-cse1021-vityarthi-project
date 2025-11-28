#Write a function is_abundant(n) that returns True if the
#sum of proper divisors of n is greater than n.

import time
import sys
import math

def is_abundant(n):
  
  if n <= 0:
    
    return False
  if n == 1:
    
    return False
    
  sum_of_proper_divisors = 1 
  
  
  limit = int(math.sqrt(n))
  
  for i in range(2, limit + 1):
    if n % i == 0:
      # i is a divisor.
      sum_of_proper_divisors += i
      
      
      if i * i != n:
        sum_of_proper_divisors += n // i

  
  return sum_of_proper_divisors > n

# --- Execution and Benchmarking ---

try:
  
  n = int(input("Enter a positive integer to check for abundance: "))

  
  start_time = time.time()
  
  
  result = is_abundant(n)
  
  
  end_time = time.time()
  
  execution_time = end_time - start_time
  
  
  print("\n------------------------------------")
  print(f"Number checked (n): {n}")
  print(f"Is {n} Abundant? **{result}**")
  print(f"Execution Time (Optimized): {execution_time:.6f} seconds")
  print("------------------------------------")

except ValueError:
  print("Error: Invalid input. Please enter a valid integer.")
except Exception as e:
  
  print(f"An error occurred: {e}")
