import time
import sys

def modular_exponentiation(base, exponent, modulus):
    
    if modulus == 1:
        return 0
    base %= modulus
    result = 1
    
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        base = (base * base) % modulus
        
        exponent //= 2
        
    return result

DETERMINISTIC_BASES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

def is_prime_miller_rabin(n: int, k: int = 5) -> bool:
 
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
        
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    bases_to_check = DETERMINISTIC_BASES[:k]
    
    for a in bases_to_check:
        if a >= n - 1:
            break 
            
        x = modular_exponentiation(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
            
        is_strong_pseudoprime = False
        for _ in range(r - 1):
            # Compute x = x^2 mod n
            x = modular_exponentiation(x, 2, n)
            
            if x == n - 1:
                # Found the strong pseudoprime condition
                is_strong_pseudoprime = True
                break
        
        if not is_strong_pseudoprime:
            # If the loop finished without finding n-1, n is definitely composite
            return False
            
    return True

# --- Example Usage and Performance Measurement ---

if __name__ == "__main__":
    # Test numbers include known primes, composites, and a large prime.
    test_numbers = [2, 7, 999983, 1000000007]
    k_bases = 10
    
    print("--- Miller-Rabin Primality Checker (Custom Implementation) ---")
    print(f"Testing with k={k_bases} deterministic bases: {DETERMINISTIC_BASES[:k_bases]}")
    
    print("\n[Test Results]")
    total_time_ms = 0
    total_memory_bytes = 0
    
    for num in test_numbers:
        # Start Timer
        start_time = time.perf_counter()
        
        try:
            is_prime = is_prime_miller_rabin(num, k=k_bases)
        except TypeError as e:
            print(f"  {num} -> Error: {e}")
            continue
            
        end_time = time.perf_counter()
        
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        memory_usage_bytes = sys.getsizeof(is_prime) # Size of the boolean result
        
        total_time_ms += elapsed_time
        total_memory_bytes += memory_usage_bytes
        
        result_str = "Likely Prime" if is_prime else "Composite"
        
        print(f"  {num}: {result_str} (Time: {elapsed_time:.6f} ms)")

    avg_time_ms = total_time_ms / len(test_numbers)
    
    print("\n[Performance Metrics Summary]")
    print(f"Total numbers tested: {len(test_numbers)}")
    print(f"Average time per check: {avg_time_ms:.6f} milliseconds")
    print(f"Approximate memory for result object (per case): {total_memory_bytes / len(test_numbers):.0f} bytes")
