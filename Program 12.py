import time
import sys

def is_prime_power(n):

    # Handle the trivial case:
    if n <= 1:
        return False
    
    temp_n = n
    prime_factor = -1
    
    # Check for factor 2
    if temp_n % 2 == 0:
        prime_factor = 2
        # Divide out all factors of 2
        while temp_n % 2 == 0:
            temp_n //= 2
            
    # Check for odd factors starting from 3 up to the square root of temp_n
    i = 3
    # Manual square root check: i * i <= temp_n
    while i * i <= temp_n:
        if temp_n % i == 0:
            
            if prime_factor != -1:
                # Found a second distinct prime factor
                return False
            
            # This is the first prime factor (and it's not 2)
            prime_factor = i
            
            # Divide out all factors of i
            while temp_n % i == 0:
                temp_n //= i
                
        # Move to the next odd number
        i += 2
        
    # Final check for the remaining number (the largest prime factor)
    if temp_n > 1:
        # Check if this new factor is distinct from the one already found.
        if prime_factor != -1 and prime_factor != temp_n:
            return False
        
        prime_factor = temp_n
        
    # If a single prime factor was successfully identified, it is a prime power.
    return prime_factor != -1

# --- Execution and Output Section ---

test_numbers = [27, 12, 16, 7, 30, 1]
print(f"**Checking Prime Power Status for Numbers:** {test_numbers}\n")

for n in test_numbers:
    # 1. Start Timer
    start_time = time.time()
    
    # 2. Execute Function and Get Output
    result = is_prime_power(n)
    
    # 3. End Timer
    end_time = time.time()
    
    # 4. Calculate Metrics
    execution_time = end_time - start_time
    # Use sys.getsizeof for the memory of the result object (True/False is 28 bytes)
    memory_usage = sys.getsizeof(result) 
    
    # 5. Print Output and Metrics
    print(f"--- Input: {n} ---")
    print(f"Output: {result}")
    
    # Note: Using a standard format like milliseconds for readability
    print(f"Execution Time: {execution_time * 1000:.4f} milliseconds")
    print(f"Memory Utilisation (Result Object): {memory_usage} bytes")
    print("-" * 20)
