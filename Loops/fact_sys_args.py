import sys

def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact

print(factorial(int(sys.argv[1])))