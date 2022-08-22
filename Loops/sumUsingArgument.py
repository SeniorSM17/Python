# Python program to demonstrate
# command line arguments

import sys

# total arguments
n = len(sys.argv)
print("Total arguments passed:", n)

# Arguments passed
print("\nName of Python script:", sys.argv[0])

print("\nArguments passed:", end = " ")

for i in range(1, n):
    print(sys.argv[i], end = " ")
    ls.append(sys.argv[i])
	
# Addition of numbers
Sum = 0
for i in range(1, n):
	Sum += int(sys.argv[i])
	
print("\n\nResult:", Sum)

def multiply(n):
    mul=1
    for i in range(1,n):
        mul*=int(sys.argv[i])
    return mul
print(multiply(n))

