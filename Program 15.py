import time
import tracemalloc

def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if i * i == n:
                count += 1
            else:
                count += 2
        i += 1
    return count
num = int(input("Enter a number: "))
tracemalloc.start()
start_time = time.time()
result = count_divisors(num)
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print(f"Number of divisors of {num}: {result}")
print(f"Execution time: {end_time - start_time:.8f} seconds")
print(f"Current memory usage: {current / 1024:.4f} KB")
print(f"Peak memory usage: {peak / 1024:.4f} KB")
