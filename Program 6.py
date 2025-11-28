import time
import sys
var=1
start_time=time.time()

def is_deficient(x):
    if x<= 0:
        print(False)
        return
    
    sum_of_divisors = 0
    for i in range(1,x):
        if x%i == 0:
            sum_of_divisors+= i
    
    if sum_of_divisors<x:
        print(True)  
    else:
        print(False)  
is_deficient(6)
is_deficient(4)  # 1,2   1+2=3, where 4>3(true is printed)

end_time=time.time()
execution_time=end_time-start_time
print("Execution time:", execution_time)
print(sys.getsizeof(var))
