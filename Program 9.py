#Write a function in python is_pronic(n) that checks if a number is
#the product of two consecutive integers.

def is_pronic(n):
    if n < 0:
        return False
    for i in range(int(n**0.5) + 1):
        if i * (i + 1) == n:
            return True
    return False
n=int(input("Enter the number:"))
print(is_pronic(n))
