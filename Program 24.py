import time
import tracemalloc

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None

    tracemalloc.start()
    start = time.time()

    k = 1
    value = a % n

    while value != 1:
        value = (value * a) % n
        k += 1
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    exec_time = time.time() - start
    mem_used = peak / 1024  

    print(f"Execution Time: {exec_time:.6f} seconds")
    print(f"Memory Used: {mem_used:.2f} KB")

    return k

a = int(input("Enter a: "))
n = int(input("Enter n: "))

result = order_mod(a, n)

if result is None:
    print("Order does not exist because a and n are not coprime.")
else:
    print(f"Order of {a} mod {n} is {result}.")
