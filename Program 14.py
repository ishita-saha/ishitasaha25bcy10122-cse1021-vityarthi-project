import time
import sys

var=1

start_time=time.time()

def is_prime(n):
    """
    Checks if a number n is prime.
    Returns True if n is prime, False otherwise.
    Note: Assumes n >= 2.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    
    while i * i <= n:
        if n % i == 0:
            return False
        i = i + 2
    return True

def twin_primes(limit):
    
    twin_pairs = []
    
    
    p = 3
    while p <= limit - 2:
        
        if is_prime(p):
            p_plus_2 = p + 2
            
            if is_prime(p_plus_2):
                twin_pairs.append((p, p_plus_2))
        
        # Move to the next odd number. 
        # All primes > 2 are odd, and since twin primes p and p+2 
        # must both be prime, p must be odd (except for the pair (3, 5)).
        # Incrementing by 2 skips even numbers, optimizing the check.
        p = p + 2
        
    return twin_pairs

# --- Example Usage ---

# Find all twin prime pairs where the larger number is up to 100
limit_value = 100
result = twin_primes(limit_value)

print(f"Twin prime pairs up to {limit_value}:")



print(result)


end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
# Expected Output:
[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43), (59, 61), (71, 73)]
