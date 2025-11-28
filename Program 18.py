import time
import sys

var=1
start_time=time.time()
def multiplicative_persistence(n):
    
    # Handle single-digit numbers immediately (persistence is 0)
    if n < 10:
        return 0

    persistence_count = 0
    
    # Main loop: Continues as long as the current number 'n' is not a single digit
    while n >= 10:
        persistence_count = persistence_count + 1
        
        # Initialize the product for the next iteration step
        next_n = 1
        
        # Inner loop: Extracts digits and calculates their product
        current_num = n
        
        # Loop while there are still digits left to process (current_num > 0)
        while current_num > 0:
            # Get the last digit using the modulo operator
            digit = current_num % 10
            
            # Multiply the digit into the product
            # Note: For efficiency, we can skip multiplying by 0, but for completeness 
            # and simplicity, we'll let multiplication by zero handle the zero case.
            next_n = next_n * digit
            
            # Remove the last digit using integer division
            current_num = current_num // 10
            
        # If at any point the product is a single digit, the next check will fail the main 'while' loop.
        # Set the current number 'n' to the product 'next_n' for the next step.
        n = next_n
        
    return persistence_count


n=int(input("Enter the number:"))
print(multiplicative_persistence(n))
end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
