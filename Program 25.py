import time
import sys

# --- Core Logic Functions (No built-in functions/modules used) ---

def is_prime(n):
    
    if n <= 1:
        return False
    if n <= 3:
        return True
    
    # Check divisibility by 2 and 3
    if n % 2 == 0 or n % 3 == 0:
        return False
        
    # Check for factors starting from 5 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True

def is_fibonacci(n):
    
    if n < 0:
        return False
    
    a, b = 0, 1
    
    # Handle the first two numbers (0 is technically Fibonacci, but 1 is often the focus)
    if n == 0 or n == 1:
        return True
        
    # Generate sequence until 'b' exceeds or equals n
    while b < n:
        a, b = b, a + b
        
    return b == n

def is_fibonacci_prime(n):
        return is_fibonacci(n) and is_prime(n)

# --- Execution and Performance Measurement ---

if __name__ == "__main__":
    
    # --- Example Test Numbers ---
    test_numbers = [1, 2,1597]
    
    for number in test_numbers:
        
        # 1. Start Performance Measurement
        start_time = time.perf_counter()
        
        
        start_mem_size = sys.getsizeof(number) 

        # 2. Execute Function
        result = is_fibonacci_prime(number)

        # 3. End Performance Measurement
        end_time = time.perf_counter()
        end_mem_size = sys.getsizeof(number)
        
        # 4. Print Results
        status = "is" if result else "is NOT"
        
        print("-" * 50)
        print(f"Checking N = {number}")
        print(f"Result: {number} {status} a Fibonacci Prime.")
        
        # Display performance metrics
        execution_time_ms = (end_time - start_time) * 1000
        memory_used_bytes = end_mem_size - start_mem_size
        
        print(f"Execution Time: {execution_time_ms:.6f} milliseconds")
        print(f"Memory Overhead (sys.getsizeof difference): {memory_used_bytes} bytes")
