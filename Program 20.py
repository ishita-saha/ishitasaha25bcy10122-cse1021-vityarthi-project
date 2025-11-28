import time
import sys

var=1

start_time=time.time()

def mod_exp(base, exponent, modulus):
    
    
    # Handle the case where the modulus is 1 (result is always 0)
    if modulus == 1:
        return 0

    # Initialize the result variable
    res = 1
    
    # We must ensure the base is within the modular range from the start
    base = base % modulus
    
    # We work with the exponent, iteratively reducing it to zero
    current_exponent = exponent
    
    # Loop until the exponent is completely processed
    while current_exponent > 0:
        
        # Check if the least significant bit of the exponent is 1 (i.e., if exponent is odd)
        # Using the modulo operator is the approved way to check parity
        if current_exponent % 2 == 1:
            # If odd, multiply the current result by the base power and apply the modulus
            # This is equivalent to multiplying by base^(2^k) where the bit is set
            res = (res * base) % modulus
        
        # Square the base and apply the modulus
        # This prepares the base for the next power of 2: base = base^(2 * previous_power)
        base = (base * base) % modulus
        
        # Integer division by 2 is equivalent to a right bit shift, preparing for the next bit
        current_exponent = current_exponent // 2
        
    return res

base=int(input("Enter the base:"))
exponent=int(input("Enter the exponent:"))
modulus=int(input("Enter the modulus:"))
print(mod_exp(base, exponent, modulus))
end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
