import time
import sys

def integer_power(base, exponent):
   
    if exponent == 0:
        return 1
    
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def integer_isqrt(n):
    
    if n < 0:
        raise ValueError("Cannot compute square root of negative number.")
    if n == 0 or n == 1:
        return n
    
    low = 1
    
    high = n // 2 + 1 
    
    result = 1
    
    while low <= high:
        mid = (low + high) // 2
        # Use simple multiplication instead of pow or **
        mid_sq = mid * mid 
        
        if mid_sq == n:
            return mid
        elif mid_sq < n:
            result = mid # Store potential answer
            low = mid + 1
        else:
            high = mid - 1
            
    return result

def is_perfect_power(n):
    
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # 1. Base Case: 1 is a perfect power
    if n == 1:
        return True

    max_a = integer_isqrt(n)
    
    b = 2 # Start checking exponents b >= 2
    
    while True:
        # Determine the maximum possible base 'a' for the current exponent 'b'
        
        low = 2
        
        high = max_a
        
        while low <= high:
            a = (low + high) // 2
            
            p = integer_power(a, b)
            
            if p == n:
                # Found the solution: n = a^b
                return True
            elif p < n:
                low = a + 1
            elif p > n:
                high = a - 1
            
        next_min_power = 2
        for i in range(b): # Calculate 2^b
            next_min_power *= 2
        
        # If 2^(b+1) > n, we stop.
        if next_min_power > n:
            break

        b += 1
        
    return False

# --- Example Usage and Performance Measurement ---

if __name__ == "__main__":
    
    test_numbers = [4, 1, 1000000, 1000001]
    
    print("--- Perfect Power Checker (No built-in math functions) ---")
    
    print("\n[Test Results]")
    total_time_ms = 0
    total_memory_bytes = 0
    
    for num in test_numbers:
        # Start Timer
        start_time = time.perf_counter()
        
        try:
            is_pp = is_perfect_power(num)
        except (TypeError, ValueError) as e:
            print(f"  {num} -> Error: {e}")
            continue
            
        # End Timer
        end_time = time.perf_counter()
        
        # Calculate performance metrics
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        memory_usage_bytes = sys.getsizeof(is_pp) # Size of the boolean result
        
        total_time_ms += elapsed_time
        total_memory_bytes += memory_usage_bytes
        
        result_str = "Perfect Power" if is_pp else "Not a Perfect Power"
        
        print(f"  {num}: {result_str} (Time: {elapsed_time:.6f} ms)")

    # Output Performance Summary
    avg_time_ms = total_time_ms / len(test_numbers)
    
    print("\n[Performance Metrics Summary]")
    print(f"Total numbers tested: {len(test_numbers)}")
    print(f"Average time per check: {avg_time_ms:.6f} milliseconds")
    print(f"Approximate memory for result object (per case): {total_memory_bytes / len(test_numbers):.0f} bytes (for the boolean result)")
