import time
import sys

def partition_function(n):
    
    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    if n == 0:
        return 1
    
    dp = [0] * (n + 1)
    dp[0] = 1 # p(0) = 1 (empty partition)

    g_k_list = []
    k = 1
    while True:
        g_k = k * (3 * k - 1) // 2
        g_minus_k = k * (3 * k + 1) // 2
        
        if g_k <= n:
            g_k_list.append(g_k)
        if g_minus_k <= n:
            g_k_list.append(g_minus_k)
        
        if g_k > n and g_minus_k > n:
            break
        
        k += 1

    for i in range(1, n + 1):
        sign_index = 0 # Used to track the sign (+1, +1, -1, -1, +1, +1, ...)
        current_sum = 0
        
        for g_k in g_k_list:
            if i - g_k < 0:
                break # All subsequent g_k will be too large
            
            sign = 1 if (sign_index % 4 < 2) else -1
            
            current_sum += sign * dp[i - g_k]
            
            sign_index += 1
            
        dp[i] = current_sum

    return dp[n]


if __name__ == "__main__":
    N_TO_CALCULATE = 100 
    
    print("--- Integer Partition Function p(n) Calculator ---")
    
    try:
        start_time = time.perf_counter()
        
        result_p_n = partition_function(N_TO_CALCULATE)
        
        end_time = time.perf_counter()
        
        elapsed_time = (end_time - start_time) * 1000  # in milliseconds
        memory_usage_bytes = sys.getsizeof(result_p_n) # Size of the integer result
        
        print(f"\n[Result: p({N_TO_CALCULATE})]")
        print(f"The number of partitions is: {result_p_n}")
        
        print("\n[Performance Metrics]")
        print(f"Time taken: {elapsed_time:.6f} milliseconds")
        print(f"Memory allocated for result (approx.): {memory_usage_bytes} bytes")

    except (TypeError, ValueError) as e:
        print("\n[Error]")
        print(e)
