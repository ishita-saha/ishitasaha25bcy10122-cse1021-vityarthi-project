import time
import sys

def digital_root_formula(n):
  
  if n < 0:
    raise ValueError("Digital root is typically defined for non-negative integers.")
  if n == 0:
    return 0
  else:
    
    return 1 + (n - 1) % 9

# --- Input Handling and Execution ---

try:
  
  n = int(input("Enter the non-negative integer: "))
  
  
  if n < 0:
    print("Error: Please enter a non-negative integer.")
  else:
    start_time_formula = time.time()
    result_formula = digital_root_formula(n)
    end_time_formula = time.time()
    execution_time_formula = end_time_formula - start_time_formula
    
    print("\n-------------------------")
    print(f"Input Number: {n}")
    print(f"Result (Formula): {result_formula}")
    print(f"Formula Execution time: {execution_time_formula:.9f} seconds")
    print("-------------------------")
    
except ValueError:
  print("Error: Invalid input. Please enter a valid integer.")
