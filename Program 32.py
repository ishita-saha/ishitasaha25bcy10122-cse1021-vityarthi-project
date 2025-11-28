import time
import sys

def gcd(a, b):
    
    a = abs(a)
    b = abs(b)
    
    if a < 0: a = -a
    if b < 0: b = -b
    
    while b:
        a, b = b, a % b
    return a

def is_prime_simple(n):
    
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    
    i = 5
    while i * i <= n and i < 20: 
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    
    return True

def pollard_rho(n):
    
    if n <= 1: return None
    if n % 2 == 0: return 2
    if is_prime_simple(n): return n # Skip for probable primes
    
    x = 2
    y = 2
    c = 1 # The constant for the polynomial f(x) = (x^2 + c) mod n
    d = 1 # Greatest Common Divisor
    
    
    max_restarts = 5
    for restart_count in range(max_restarts):
        x = restart_count + 2 # Different start point
        y = x
        c = restart_count + 1 # Different constant
        d = 1
        limit = 100000 # Safety limit for iterations
        
        for i in range(1, limit):
            x = (x * x + c) % n
            
            y = (y * y + c) % n
            y = (y * y + c) % n
            
            diff = x - y
            if diff < 0:
                diff = -diff # Manual abs
            
            d = gcd(diff, n)
            
            if d > 1:
                if d == n:
                    break
                else:
                    return d
        
        if d > 1 and d < n:
            return d

    return n


if __name__ == "__main__":
    

    test_numbers = [91, 10403, 863, 29017]
    
    print("--- Pollard's Rho Factorization ---")

    for number in test_numbers:
        
        start_time = time.perf_counter()
        
        start_mem_size = sys.getsizeof(number) 

        factor = pollard_rho(number)

        end_time = time.perf_counter()
        end_mem_size = sys.getsizeof(number)
        
        print("-" * 50)
        print(f"Factoring N = {number}")
        
        if factor is None:
            result_msg = "Cannot factor (Input <= 1)."
        elif factor == number:
            result_msg = f"No non-trivial factor found (N is likely prime: {number})."
        else:
            other_factor = number // factor
            result_msg = f"Factor found: {factor}. Other factor: {other_factor}."
        
        print(f"Result: {result_msg}")
        
    
        execution_time_ms = (end_time - start_time) * 1000
        memory_used_bytes = end_mem_size - start_mem_size
        
        print(f"Execution Time: {execution_time_ms:.6f} milliseconds")
        print(f"Memory Overhead (sys.getsizeof difference): {memory_used_bytes} bytes")
        
    print("-" * 50)
