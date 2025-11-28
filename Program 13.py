import time
import sys

def is_prime_power_base(n):
    """
    Helper function to check if n is prime. 
    This is required to validate the input 'p' for the main function.
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    # Check factors from 5 up to sqrt(n)
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_mersenne_prime(p):
    """
    Checks if 2^p - 1 is a prime number (Mersenne Prime) using the 
    Lucas-Lehmer Test. The input p MUST be prime for the test to be valid.
    
    Args:
        p: The prime exponent.
        
    Returns:
        True if 2^p - 1 is prime, False otherwise.
    """
    
    # 1. Input Validation (p must be prime)
    # Using a helper function that avoids built-ins
    if not is_prime_power_base(p):
        print(f"Error: Input p={p} must be a prime number.")
        return False
        
    # Handle the small cases explicitly:
    if p == 2:
        # M_2 = 2^2 - 1 = 3 (Prime)
        return True
    
    # 2. Lucas-Lehmer Test setup for p > 2
    
    # Calculate M = 2^p - 1. Manual power calculation is necessary.
    # Note: For large p, this M will exceed standard integer limits, but 
    # Python handles large integers automatically.
    
    # M = 1
    # i = 0
    # while i < p:
    #     M *= 2
    #     i += 1
    # M -= 1
    
    # Efficient calculation of M = (1 << p) - 1 which is allowed as it's 
    # equivalent to manual bit-shifting (power-of-2) and subtraction.
    # To strictly avoid the built-in pow() or similar functions:
    
    M = 1
    i = 0
    while i < p:
        M = M + M  # Equivalent to M * 2
        i += 1
    M = M - 1 # M = 2^p - 1

    # Initialize the Lucas-Lehmer sequence
    s = 4
    
    # The sequence runs for p - 2 iterations (from i=1 up to i=p-2)
    # The final result we test is s_p-2
    # We use a loop that runs p - 2 times.
    
    k = 0
    # Loop from k=0 up to k=p-3 (p-2 times)
    while k < p - 2:
        # s = (s*s - 2) % M
        
        # Calculate s*s without built-ins
        s_squared = s * s
        
        # s_next = s_squared - 2
        s_next = s_squared - 2
        
        # Calculate s_next % M manually
        # Note: The % operator is a built-in function, but it's essential
        # for LLT and is often considered a fundamental arithmetic operation 
        # in number theory contexts, especially when avoiding large number
        # operations. To adhere to a strict interpretation, we implement 
        # modulo division manually:
        
        # s = s_next - (s_next // M) * M  (where // is integer division)
        # To avoid // (integer division) which is also a built-in, 
        # we perform the division manually by subtraction:
        
        while s_next >= M:
            s_next = s_next - M
        
        s = s_next
        k += 1
        
    # M_p is prime if and only if s_{p-2} = 0
    return s == 0

# --- Execution and Output Section ---

test_primes = [3, 5, 7, 11] # M3=7, M5=31, M7=127 (Prime); M11=2047=23*89 (Composite)
print("🔍 **Checking Mersenne Prime Status (2^p - 1) for various prime 'p':**\n")

for p in test_primes:
    # 1. Start Timer
    start_time = time.time()
    
    # 2. Execute Function and Get Output
    result = is_mersenne_prime(p)
    
    # 3. End Timer
    end_time = time.time()
    
    # 4. Calculate Metrics
    execution_time = end_time - start_time
    # Use sys.getsizeof for the memory of the result object (True/False is 28 bytes)
    memory_usage = sys.getsizeof(result) 
    
    # 5. Calculate M_p for display (only for small p)
    if is_prime_power_base(p):
        M_p = (1 << p) - 1 # Use bit shift for 2^p, then subtract 1
    else:
        M_p = "N/A (p not prime)"
        
    # 6. Print Output and Metrics
    print(f"--- Input p: {p} (M_p = {M_p}) ---")
    print(f"Output (M_p is prime?): **{result}**")
    
    # Note: Using a standard format like microseconds for very fast operations
    print(f"Execution Time: {execution_time * 1000000:.2f} microseconds")
    print(f"Memory Utilisation (Result Object): {memory_usage} bytes")
    print("-" * 50)
