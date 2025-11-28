import time
import sys

def collatz_length(n):
    
    if n <= 0:
        
        raise ValueError("Input must be a positive integer.")
    
    current = n
    steps = 0
    
    while current != 1:
        
        if current % 2 == 0:
            # If even, divide by 2
            current = current // 2  # Integer division is used
        else:
            # If odd, apply (3 * n + 1)
            current = 3 * current + 1
        
        steps += 1
        
        if steps > 100000:
            
            print(f"Warning: Reached max steps (100000) for starting number {n}")
            return -1 # Return -1 to indicate failure or max limit reached

    return steps

# --- Execution and Performance Measurement ---

if __name__ == "__main__":
    
    # --- Example Test Numbers ---
    test_numbers = [6, 100, 27]
    
    print("--- Collatz Sequence Length Calculation ---")

    for number in test_numbers:
        
        start_time = time.perf_counter()
        
        start_mem_size = sys.getsizeof(number) 

        try:
            result_steps = collatz_length(number)
        except ValueError as e:
            print("-" * 50)
            print(f"Checking N = {number}")
            print(f"Error: {e}")
            continue

        end_time = time.perf_counter()
        end_mem_size = sys.getsizeof(number)
        
        print("-" * 50)
        print(f"Checking N = {number}")
        
        if result_steps != -1:
            print(f"Steps required to reach 1: {result_steps}")
        else:
            print("Calculation failed or exceeded safety limit.")
        
        execution_time_ms = (end_time - start_time) * 1000
        memory_used_bytes = end_mem_size - start_mem_size
        
        print(f"Execution Time: {execution_time_ms:.6f} milliseconds")
        
        print(f"Memory Overhead (sys.getsizeof difference): {memory_used_bytes} bytes")
        
    print("-" * 50)
