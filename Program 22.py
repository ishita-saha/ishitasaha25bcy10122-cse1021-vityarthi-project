import time
import sys

# --- Helper Functions for CRT ---

def extended_gcd(a, b):
    """
    Implements the Extended Euclidean Algorithm (EEA).
    Finds g = gcd(a, b) and integers x, y such that a*x + b*y = g.
    Returns (g, x, y)
    """
    if a == 0:
        return (b, 0, 1)
    
    g, x1, y1 = extended_gcd(b % a, a)
    
    # Update x and y using results from recursive call
    x = y1 - (b // a) * x1
    y = x1
    
    return (g, x, y)

def mod_inverse(a, m):
    """
    Calculates the modular multiplicative inverse of a modulo m.
    Returns x such that a*x ≡ 1 (mod m).
    Raises ValueError if the inverse does not exist (i.e., gcd(a, m) != 1).
    """
    g, x, y = extended_gcd(a, m)
    
    if g != 1:
        # Inverse exists only if a and m are coprime
        raise ValueError(f"Modular inverse does not exist (gcd({a}, {m}) = {g} != 1). Moduli must be pairwise coprime for this simple CRT formula.")
    
    # x is the solution, normalized to be positive in the range [0, m-1]
    return x % m

# --- Main CRT Solver ---

def crt(remainders, moduli):
    """
    Solves a system of congruences using the Chinese Remainder Theorem (CRT).
    The system is x ≡ ri (mod mi) for all i.
    
    Assumes all moduli are pairwise coprime.
    
    :param remainders: A list of integers (r1, r2, ...).
    :param moduli: A list of pairwise coprime integers (m1, m2, ...).
    :return: The smallest non-negative integer solution x.
    """
    if len(remainders) != len(moduli):
        raise ValueError("The number of remainders must match the number of moduli.")

    # 1. Calculate N, the product of all moduli (M in the formula)
    N = 1
    for m in moduli:
        N *= m
    
    # 2. Calculate the solution x
    x = 0
    
    for r_i, m_i in zip(remainders, moduli):
        # M_i = N / m_i
        M_i = N // m_i
        
        # y_i = modular inverse of M_i modulo m_i
        try:
            y_i = mod_inverse(M_i, m_i)
        except ValueError as e:
            # Re-raise the error from mod_inverse for clarity
            raise e 
        
        # Add the component to the solution: r_i * M_i * y_i
        x += r_i * M_i * y_i
        
    # 3. The final answer is x mod N
    return x % N


# --- Example Usage and Performance Measurement ---

if __name__ == "__main__":
    # Example System:
    # x ≡ 2 (mod 3)
    # x ≡ 3 (mod 5)
    # x ≡ 2 (mod 7)
    
    R = [2, 3, 2] # Remainders (r_i)
    M = [3, 5, 7] # Moduli (m_i)
    
    print("--- Chinese Remainder Theorem Solver ---")
    print(f"System of congruences: x ≡ {R[0]} (mod {M[0]}), x ≡ {R[1]} (mod {M[1]}), x ≡ {R[2]} (mod {M[2]})")

    # Start Timer
    start_time = time.perf_counter()
    
    try:
        # Solve the system
        solution = crt(R, M)
        
        # End Timer
        end_time = time.perf_counter()
        
        # Calculate performance metrics
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        
        # Calculate memory usage for the result object (approximate)
        memory_usage_bytes = sys.getsizeof(solution)
        
        # Output Results
        print("\n[Result]")
        print(f"The unique solution modulo N={M[0]*M[1]*M[2]} is: x = {solution}")
        
        # Verification
        print("\n[Verification]")
        is_correct = True
        for r, m in zip(R, M):
            if solution % m == r:
                print(f"  {solution} ≡ {r} (mod {m}) - OK")
            else:
                print(f"  {solution} ≡ {solution % m} (mod {m}) - ERROR! Expected {r}")
                is_correct = False

        if is_correct:
             print("The solution is verified to be correct.")
        
        # Output Performance
        print("\n[Performance Metrics]")
        print(f"Time taken: {elapsed_time:.6f} milliseconds")
        print(f"Memory allocated for solution (approx.): {memory_usage_bytes} bytes")

    except ValueError as e:
        print(f"\n[Error]")
        print(e)
        print("Please ensure all moduli are pairwise coprime (i.e., gcd(m_i, m_j) = 1 for i != j).")
