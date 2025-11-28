import time
import sys


def integer_power(base, exponent):
    
    if exponent == 0:
        return 1.0
    
    result = 1.0
    float_base = float(base) 
    
    for _ in range(exponent):
        result *= float_base
    return result

def zeta_approx(s, terms):
    
    if not isinstance(s, int) or not isinstance(terms, int):
        raise TypeError("s and terms must be integers for this constrained implementation.")
    if s <= 1:
        raise ValueError("s must be greater than 1 for series convergence.")
    if terms <= 0:
        return 0.0

    zeta_sum = 0.0
    for n in range(1, terms + 1):
        n_to_s = integer_power(n, s)
        
        term = 1.0 / n_to_s
        
        zeta_sum += term
        
    return zeta_sum

if __name__ == "__main__":
    S = 2
    TERMS = 10000 
    
    print("--- Riemann Zeta Approximation ---")
    
    try:
        start_time = time.perf_counter()
        
        approximation = zeta_approx(s=S, terms=TERMS)
        
        end_time = time.perf_counter()
        
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        memory_usage_bytes = sys.getsizeof(approximation) # Size of the float result
        
        print(f"\n[Result: ζ({S}) Approximation]")
        print(f"Terms summed (n): {TERMS}")
        print(f"Approximated value: {approximation:.10f}")
        
        print("\n[Performance Metrics]")
        print(f"Time taken: {elapsed_time:.6f} milliseconds")
        print(f"Memory allocated for result (approx.): {memory_usage_bytes} bytes")

    except (TypeError, ValueError) as e:
        print("\n[Error]")
        print(e)
