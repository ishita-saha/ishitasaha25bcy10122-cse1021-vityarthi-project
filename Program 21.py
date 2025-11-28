import time
import sys
# import tracemalloc # for more detailed memory snapshots

def mod_inverse(a: int, m: int) -> int:
    # ... (function body as defined by user)
    if not isinstance(a, int) or not isinstance(m, int):
        raise TypeError("Both a and m must be integers.")
    if m <= 1:
        raise ValueError("Modulus m must be greater than 1.")

    def extended_gcd(x, y):
        if y == 0:
            return x, 1, 0
        gcd, x1, y1 = extended_gcd(y, x % y)
        return gcd, y1, x1 - (x // y) * y1

    gcd, x, _ = extended_gcd(a, m)

    if gcd != 1:
        raise ValueError(f"No modular inverse exists for a={a} and m={m} (gcd={gcd}).")

    return x % m

def run_test(a, m):
    # Time profiling setup
    start_time = time.perf_counter()
    
    # Memory check (sys.getsizeof is not a true profiler but provides object size)
    # The extended_gcd function uses recursion, and memory is released upon return,
    # making line-by-line memory profiling complex without external libraries.
    # We can check the size of the function object itself, which is constant.
    
    try:
        # Measure size before call (for general reference, not true profiling)
        function_size_bytes = sys.getsizeof(mod_inverse)
        
        result = mod_inverse(a, m)
        end_time = time.perf_counter()
        
        print(f"mod_inverse({a}, {m}) result: {result}")
        print(f"  Time elapsed: {end_time - start_time:.6f} seconds")
        print(f"  mod_inverse object size: {function_size_bytes} bytes (not runtime memory usage)")
        
    except (ValueError, TypeError) as e:
        end_time = time.perf_counter()
        
        print(f"mod_inverse({a}, {m}) Error: {e}")
        print(f"  Time elapsed: {end_time - start_time:.6f} seconds")

# Running the tests
run_test(3, 15)
run_test(10, 18)

# Example where the inverse exists (for comparison)
run_test(3, 11)
