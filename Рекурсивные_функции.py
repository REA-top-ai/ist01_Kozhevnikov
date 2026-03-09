# Задание 1
def factorial_recurse(n):
    if n>=0:
        if n==0 or n==1:
            return 1
        return n*factorial_recurse(n-1)

def factorial_iter(n):
    k=1
    for i in range(2,n+1):
        k*=i
    return k

# Задание 2
def square_list(numbers):
    return [n ** 2 for n in numbers]

