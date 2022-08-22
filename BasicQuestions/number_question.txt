# 1. Write a program to find sum of number.

def sum_number(number_list):
    '''Function takes number_list and
    sums it up and return sum of all the integer numbers
    '''
    sums = 0
    for numbers in number_list:
        sums += numbers
    return sums


def user_input(list_lenght):
    '''It takes the lenght of list from user and
    then take the numbers store it in list.
    Only integer type data is accepted
    '''
    number_list = []
    for i in range(list_lenght):
        number = int(input())
        number_list.append(number)
    return number_list


list_lenght = int(input("Enter Lenght of list "))
inputs = user_input(list_lenght)
result = sum_number(inputs)
print("The sum of given numbers is", result)

''' ====OUTPUT====
(base) C:\Users\\sm22227\\Documents\\Shubham\\Python\\Office Task>python 22_07_2022.py
Enter Lenght of list 5
7
8
9
3
5
The sum of given numbers is 32
'''
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# 2. WAP to find the number is strong number or not


def factorial(number):
    '''Factorial of Number is calculated and returned
    '''
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact


def strong_number(number):
    ''' Number is seperated into digits and
    factorial is calculated using factorial fucntion,
    Then sum of all individual factorial is returned
    '''
    sums = 0
    while number > 0:
        single_number = number % 10
        sums += factorial(single_number)
        number = int(number / 10)
    return sums


number = int(input("Enter a number to check Strong Number"))
if number == strong_number(number):
    print("Given Number is Strong")
else:
    print("Given Number is not a Strong Number")

''' ====OUTPUT====
(base) C:\Users\\sm22227\\Documents\\Shubham\\Python\\Office Task>python Executionfile.py
Enter a number to check Strong Number145
Given Number is Strong

(base) C:\Users\\sm22227\\Documents\\Shubham\\Python\\Office Task>python Executionfile.py
Enter a number to check Strong Number 123
Given Number is not a Strong Number
'''
# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# 3.Python Program to Find the Square Root


def square_root(number):
    ''' Takes Number as input and
    returns square root of that number
    '''
    return number ** 0.5


number = int(input("Enter the Number "))
print("Square root of ", number, " is ", square_root(number))

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# 4.Python Program to Calculate the Area of a Triangle

base = float(input("Enter base "))s
height = float(input("Enter Height "))


def area_triangle(base, height):
    '''Calculate area of triangle using formula
    area = 1/2 * base * height
    Functions returns area
    '''
    return 0.5 * base * height


print("Area of Triangle is ", area_triangle(base, height))

''' ====OUTPUT====
(base) C:\Users\\sm22227\\Documents\\Shubham\\Python\\Office Task>python Executionfile.py
Enter base 2
Enter Height 3
Area of Triangle is s 3.0
'''

# = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = = =
# 5. Python Program to Solve Quadratic Equation

''' === INFORMATION ===
The standard form of a quadratic equation is:

ax2 + bx + c = 0, where
a, b and c are real numbers and
a ≠ 0
The solutions of this quadratic equation is given by:

(-b ± (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
'''


def quadratic_solution(number_1, number_2, constant):
    '''Calculates the solution using above mention
    mathmetical formula
    '''
    discriminant = (number_2**2) - (4 * number_1 * constant)
    solution1 = (-number_2 - (discriminant**0.5)) / (2 * discriminant)
    solutions2 = (-number_2 + (discriminant**0.5)) / (2 * discriminant)
    return solution1, solutions2


number_1, number_2, constant = map(float, input(
    "Enter number_1,number_2,constant").split())
print("The Solutions are", quadratic_solution(number_1, number_2, constant))

''' ===OUTPUT===
(base) C:\Users\\sm22227\\Documents\\Shubham\\Python\\Office Task>python Executionfile.py
Enter number_1,number_2,constant 3 4 5
The Solutions are ((0.045454545454545456+0.07537783614444091j), (0.04545454545454545-0.07537783614444091j))
'''

# 6.Python Program to Swap Two Variables


def swap_numbers(number_1, number_2):
    ''' The following fucntion swaps their data
    among them'''
    temp = number_1
    number_1 = number_2
    number_2 = temp
    return number_1, number_2


number_1 = float(input("Enter 1st Number"))
number_2 = float(input("Enter 2nd Number"))
print(swap_numbers(number_1, number_2))


''' ===OUTPUT===
PS C:\Users\\shubh\\Downloads> python .\\Execution.py
(20, 10)
PS C:\Users\\shubh\\Downloads> python .\\Execution.py
Enter 1st Number20
Enter 2nd Number10
(10.0, 20.0)
'''

# 7.Python Program to Convert Kilometres to Miles


def conversion_km_miles(km):
    ''' 1km = 0.62137119 Miles
    '''
    return km * 0.62137119


km = float(input("Enter the Kilometer"))
print(km, "Kilometer = ", conversion_km_miles(km))


''' ===OUTPUT===
PS C:\Users\\shubh\\Downloads> python .\\Execution.py
Enter the Kilometer 10
10.0 Kilometer =  6.2137119
PS C:\Users\\shubh\\Downloads> python .\\Execution.py
Enter the Kilometer 10.10
10.1 Kilometer =  6.275849019
'''

# 8. Python Program to Check Leap Year 


def leap_year(year):
    if year %400 ==0 and year %100 ==0 :
        print(year," is a leap year.")
    elif year %4==0 and year %100 !=0:
        print(year," is a leap year.")
    else:
        print(year," is not a leap year.")


year=int(input("Enter the year"))
leap_year(year)

''' === OUTPUT ===
PS C:\Users\shubh\Downloads> python .\Execution.py
Enter the year 2020
2020  is a leap year.
PS C:\Users\shubh\Downloads> python .\Execution.py
Enter the year2021
2021  is not a leap year.
'''

# 9.Python Program to Check Prime Number 

def is_Prime(number):
    ''' The function will take input as number 
    and check if number is prime or not 
    '''
    flag=True
    for num in range(2,number):
        if number%num ==0:
            flag =False
        else:
            pass
    if flag :
        print("Number is Prime")
    else:
        print("Number not Prime")
    
number = int(input("Enter the number"))
is_Prime(number)


''' ===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number5
Number is Prime

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number4
Number not Prime

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number 155
Number not Prime

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number17
Number is Prime

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number11
Number is Prime
'''

# 10. Python Program to Find the Factorial of a Number 

def fact(number):
    ''' Return factorial of number
    '''
    sums=1
    for numbers in range(0,number):
        sums*=number
    return sums
    
number=int(input("Enter the number ))
factorials=fact(number)
print("Factorial of a number is ,", factorials)

''' ===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number 6
Factorial of a number is , 720

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number 5
Factorial of a number is , 120
'''


# 11. Python Program to Print the Fibonacci sequence 

def fibo_sequence(number):
    ''' Function will print 
    FIbonacci Sequence 
    '''
    print("Fibonacci Sequence is")
    for i in range(number,0,-1):
        print(i,end=",")

number=int(input("Enter the number"))
fibo_sequence(number)

''' ===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number10
Fibonacci Sequence is
10,9,8,7,6,5,4,3,2,1,
'''

# 12. Armstrong NUmber
def length_number(number):
    ln=0
    list_number=[]
    while number >0:
        ln+=1
        if number == 0:
            break
        list_number.append(number%10)
        number=(number//10)
    return ln,list_number

def armstrong_number(number):
    ln,list_number=length_number(number)
    armstrong_number=0
    for element in list_number:
        armstrong_number+= (element**ln)
    if armstrong_number == number:
        print("NUmber is armstrong number")
        return number
    else:
        print("Not armstrong_number")

number = 371
print(armstrong_number(number))


''' 
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Not armstrong_number

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
NUmber is armstrong number

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
NUmber is armstrong number

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Not armstrong_number

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
NUmber is armstrong number

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
NUmber is armstrong number
371
'''

# 13.Python Program to Find Armstrong Number in an Interval 

def length_number(number):
    ln=0
    list_number=[]
    while number >0:
        ln+=1
        if number == 0:
            break
        list_number.append(number%10)
        number=(number//10)
    return ln,list_number

def armstrong_number(number):
    temp=number
    ln,list_number=length_number(number)
    armstrong_number=0
    for element in list_number:
        armstrong_number+= (element**ln)
    return armstrong_number

start=int(input("Enter the Start value of range"))
end=int(input("Enter the End value of range"))
for i in range(start,end):
    if armstrong_number(i)==i:
        print(i,end=",")


''' ===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the Start value of range0
Enter the End value of range1000
0
1
2
3
4
5
6
7
8
9
153
370
371
407

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the Start value of range0
Enter the End value of range10000
0,1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474,
'''

# 14.Python Program to Find the Sum of Natural Numbers 


number=int(input("Enter the number for sum"))
print("Sum of natural number is", (number*(number+1))/2)

''' ===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number for sum6
Sum of natural number is 21.0

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number for sum4
Sum of natural number is 10.0
'''

# 15.Python Program to Find the Factors of a Number 

number=int(input("Enter the number for factors")
for i in range(1,number+1):
    if number %i ==0 :
        print(i,end=" ")
        
''' ===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number for factors 12
The Factors are
1 2 3 4 6 12
(base) C:\Userss\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number for factors 100
The Factors are
1 2 4 5 10 20 25 50 100
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter the number for factors987654321
The Factors are
1 3 9 17 51 153 289 867 2601 379721 1139163 3417489 6455257 19365771 58097313 109739369 329218107 987654321
'''

# 16.Python Program to Convert Decimal to Binary, Octal and Hexadecimal 
'''dec = int(input("Enter the Decimal Value")
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
'''

def dec_binary(dec):
    a=[]
    while(dec>0):
        dig=dec%2
        a.append(dig)
        dec=dec//2
    a.reverse()
    print("Binary Equivalent is: ")
    for i in a:
        print(i,end=" ")

def dec_octa(num):
    b=[]
    while(num>0):
        dig=num%8
        b.append(dig)
        num=num//8
    b.reverse()
    print("Binary Equivalent is: ")
    for i in b:
        print(i,end=" ")  
    

conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
def decimalToHexadecimal(decimal):
    hexadecimal = ''
    while(decimal > 0):
        remainder = decimal % 16
        hexadecimal = conversion_table[remainder] + hexadecimal
        decimal = decimal // 16

    return hexadecimal


decimal_number=int(input("ENter a decimal Number"))
print("The hexadecimal form of", decimal_number,
      "is", decimalToHexadecimal(decimal_number))

dec_binary(decimal_number)
dec_octa(decimal_number)


'''===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python h2.py
ENter a decimal Number12
The hexadecimal form of 12 is C
Binary Equivalent is:
1 1 0 0 Binary Equivalent is:
1 4

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python h2.py
ENter a decimal Number 15
The hexadecimal form of 15 is F
Binary Equivalent is:
1 1 1 1 Binary Equivalent is:
1 7
'''
# 17. LCM

def lcm(num1, num2):
   if num1 > num2:
       greater = num1
   else:
       greater = num2

   while(True):
       if((greater % num1 == 0) and (greater % num2 == 0)):
           lcm = greater
           break
       greater += 1

   return lcm
   
num1,num2=map(int,input("Enter two numbers").split())
print(lcm(num1,num2))

'''===OUTPUT===
(base) C:\Users\sm22227\Documents\Shubham\Pnum2thon\Office Task>pnum2thon Enum1ecutionfile.pnum2
Enter two numbers 10 12
60
'''

#18 HCF

def hcf(num1, num2):
    if num1 > num2:
        smaller = num2
    else:
        smaller = num1
    for i in range(1, smaller+1):
        if((num1 % i == 0) and (num2 % i == 0)):
            hcf = i 
    return hcf

num1,num2=map(int,input("Enter two numbers").split())
print(hcf(num1,num2))

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python Executionfile.py
Enter two numbers 10 12
2
'''