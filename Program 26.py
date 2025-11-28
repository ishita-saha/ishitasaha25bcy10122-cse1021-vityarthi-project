import time
import sys

def lucas_sequence(n):
    """
    Generates the first n terms of the Lucas sequence (L_n).
    Initial terms are L_0 = 2, L_1 = 1. Recurrence is L_n = L_{n-1} + L_{n-2}.
    
    :param n: The number of terms to generate (non-negative integer).
    :return: A list containing the first n Lucas numbers.
    """
    # Input validation
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    # Base cases
    if n == 0:
        return []
    elif n == 1:
        return [2]
    elif n == 2:
        return [2, 1]

    # Initialize with the first two terms
    lucas_nums = [2, 1]

    # Generate subsequent terms using the recurrence relation
    for _ in range(2, n):
        # The next number is the sum of the last two
        lucas_nums.append(lucas_nums[-1] + lucas_nums[-2])

    return lucas_nums

if __name__ == "__main__":
    # The number of terms to generate
    terms = 15
    
    print(f"--- Lucas Sequence Generation (First {terms} terms) ---")

    try:
        # Start Timer
        start_time = time.perf_counter()
        
        # Execute the function
        sequence = lucas_sequence(terms)
        
        # End Timer
        end_time = time.perf_counter()
        
        # Calculate performance metrics
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        
        # Calculate memory usage (for the list object itself)
        # Note: sys.getsizeof() returns the size of the list structure, 
        # not the memory size of all elements recursively.
        memory_usage_bytes = sys.getsizeof(sequence)
        
        # Output Results
        print("\n[Result]")
        print(f"Lucas numbers: {sequence}")

        # Output Performance
        print("\n[Performance Metrics]")
        print(f"Terms calculated: {terms}")
        print(f"Time taken: {elapsed_time:.6f} milliseconds")
        print(f"Memory allocated for list object (approx.): {memory_usage_bytes} bytes")

    except (TypeError, ValueError) as e:
        print("\n[Error]")
        print(e)
