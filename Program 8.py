import time
import sys
var=1
start_time=time.time()

def is_automorphic(n):
    square = n * n
    return str(square).endswith(str(n))

num = int(input("Enter a number: "))

if is_automorphic(num):
    print(num, "is an automorphic number.")
else:
    print(num, "is not an automorphic number.")

end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
