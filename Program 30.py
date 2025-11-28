import time
import sys

def gcd(a, b):
    
    while b:
        a, b = b, a % b
    return a

def modular_exponentiation(base, exponent, modulus):
    
    base %= modulus
    result = 1
    
    while exponent > 0:
        # If exponent is odd, multiply the result with the current base
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        base = (base * base) % modulus
        
        exponent //= 2
        
    return result

def is_composite(n):
    
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    
    i = 5
    # The while loop condition 'i * i <= n' avoids using math.sqrt()
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
        
    return False

# --- Main Carmichael Check Function ---

def is_carmichael(n):
    
    if not isinstance(n, int) or n < 2:
        raise ValueError("n must be an integer >= 2.")

    if not is_composite(n):
        return False

    exponent = n - 1
    
    for a in range(2, n):
        # Check if a is coprime to n
        if gcd(a, n) == 1:
            # Check the congruence a^(n-1) ≡ 1 (mod n)
            result = modular_exponentiation(a, exponent, n)
            
            if result != 1:
                # Congruence failed for a coprime 'a', so n is NOT a Carmichael number
                return False
                
    return True

# --- Example Usage and Performance Measurement ---

if __name__ == "__main__":
    
    test_numbers = [561, 6, 1729, 13]
    
    print("--- Carmichael Number Checker (No built-in math functions) ---")
    
    print("Note: Checking all coprime bases 'a' up to n can be slow for large n.")
    
    print("\n[Test Results]")
    total_time_ms = 0
    total_memory_bytes = 0
    
    for num in test_numbers:
        # Start Timer
        start_time = time.perf_counter()
        
        try:
            is_carm = is_carmichael(num)
        except ValueError as e:
            print(f"  {num} -> Error: {e}")
            continue
            
        end_time = time.perf_counter()
        
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        memory_usage_bytes = sys.getsizeof(is_carm) # Size of the boolean result
        
        total_time_ms += elapsed_time
        total_memory_bytes += memory_usage_bytes
        
        result_str = "Carmichael Number" if is_carm else "Not a Carmichael Number"
        
        print(f"  n = {num}: {result_str} (Time: {elapsed_time:.6f} ms)")

    avg_time_ms = total_time_ms / len(test_numbers)
    
    print("\n[Performance Metrics Summary]")
    print(f"Total numbers tested: {len(test_numbers)}")
    print(f"Average time per check: {avg_time_ms:.6f} milliseconds")
    print(f"Approximate memory for result object (per case): {total_memory_bytes / len(test_numbers):.0f} bytes")
