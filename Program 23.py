import time
import sys

def is_quadratic_residue(a, p):
    
    if not isinstance(p, int) or p <= 0:
        raise ValueError("Modulus 'p' must be a positive integer (ideally a prime for this context).")
        
    # 1. Handle Trivial Case: a ≡ 0 (mod p)
    # x^2 ≡ 0 (mod p) always has solution x=0.
    if a % p == 0:
        return True

    
    if p == 2:
        return True # Since a % p != 0 case is handled above, a must be 1 (mod 2) here.
    
    exponent = (p - 1) // 2
    
    # Use the highly optimized built-in modular exponentiation function
    legendre_symbol_value = pow(a, exponent, p)
    
    
    if legendre_symbol_value == 1:
        return True
    
    # Check if the result is p-1 (which is -1 mod p) (quadratic non-residue)
    elif legendre_symbol_value == p - 1:
        return False
    
    
    else:
                return False 


# --- Example Usage and Performance Measurement ---

if __name__ == "__main__":
    # Test cases:
    # Prime p=7. Quadratic residues are 1, 2, 4. (1^2=1, 3^2=9≡2, 2^2=4)
    P = 7
    
    test_cases = [
        (1, P),  # 1^2 ≡ 1 (mod 7) -> Residue (True)
        (2, P),  # 3^2 ≡ 2 (mod 7) -> Residue (True)
        (3, P),  # 3 is not a residue (False)
        (4, P),  # 2^2 ≡ 4 (mod 7) -> Residue (True)
        (5, P),  # 5 is not a residue (False)
        (6, P),  # 6 is not a residue (False)
        (0, P),  # Trivial case: 0 ≡ 0 (mod 7) -> Residue (True)
    ]
    
    print("--- Quadratic Residue Checker (using Euler's Criterion) ---")
    print(f"Checking residues modulo P = {P}")
    
    print("\n[Test Results]")
    total_time_ms = 0
    total_memory_bytes = 0
    
    for a, p in test_cases:
        # Start Timer
        start_time = time.perf_counter()
        
        # Execute the function
        is_residue = is_quadratic_residue(a, p)
        
        # End Timer
        end_time = time.perf_counter()
        
        # Calculate performance metrics
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        memory_usage_bytes = sys.getsizeof(is_residue) # Size of the boolean result
        
        total_time_ms += elapsed_time
        total_memory_bytes += memory_usage_bytes
        
        result_str = "Residue" if is_residue else "Non-Residue"
        
        print(f"  x^2 ≡ {a} (mod {p}) is {result_str} (Time: {elapsed_time:.4f} ms)")

    # Output Performance Summary
    avg_time_ms = total_time_ms / len(test_cases)
    
    print("\n[Performance Metrics Summary]")
    print(f"Total test cases run: {len(test_cases)}")
    print(f"Average time per check: {avg_time_ms:.6f} milliseconds")
    print(f"Approximate memory for result object (per case): {total_memory_bytes / len(test_cases):.0f} bytes (for the boolean result)")
