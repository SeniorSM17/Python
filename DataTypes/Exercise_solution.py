# 1.
# Calculate income tax for the given income by adhering to the below rules
# Taxable Income    Rate (in %)
# First $10,000    0
# Next $10,000    10
# The remaining    20
# Expected Output:
# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.
#===============================================================================
income=float(input("Enter your income "))
if income>0 and income<=10000:
    print("You have no income tax\nEnjoy Brother")
elif income>10000 and income<=20000:
    income=income-10000
    tax=(income*0.10)
    print("You owe me {0},$ \nPay or else I will kill you".format(tax))
elif income>20000:
    income = income-20000
    tax=income*0.20 + 1000
    print("You make alot of money, and you owe me,",tax,"$ of tax. \nPay now or I will kill you wife.") 


# 2.Count the length of list with out using any inbuilt function.
ls=[12,23,4,56,78,88]
count=0
for i in ls:
    count+=1
print("Length of list is :",count)

# 3.Write a Python program to create a histogram from a given list of integers.

ls=[2,3,4,5,6,7,8,8]
for i in ls:
    print("x"*i)
    
''' OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
xx
xxx
xxxx
xxxxx
xxxxxx
xxxxxxx
xxxxxxxx
xxxxxxxx
'''

# 5.Python program to check if a string is palindrome or not

strings=input("Enter the sting")
if strings==strings[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
''' OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the stingaba
Palindrome

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the stingaggavsgvags
Not Palindrome
'''

# 4. Take input from user and if input is string print String
# if input is integer/float print integer
# if input is mix of string and integer print Error
# HINT Can be done using ASCII code

inpt=input("Enter the string ")
int_counter=0
str_counter=0
for i in inpt:
    if ord(i)>48 and ord(i)<57:
        int_counter+=1
    elif (ord(i)>97 and ord(i)<122) or (ord(i)>65 and ord(i)<90) :
        str_counter+=1

if int_counter >0 and str_counter ==0:
    print("Integer")
elif int_counter == 0 and str_counter >0:
    print("String")
else:
    print("Error")
    
''' OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python try.py
Enter the string  qwertyui
String

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python try.py
Enter the string 1234567
Integer

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python try.py
Enter the string 2w34er5t6y7u89
Error

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python try.py
Enter the string u2di4hr73g48rg7834gt78gf7843re
Error

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python try.py
Enter the string 123456789
Integer

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python try.py
Enter the string AWSERDFGHJedfrgbhnjkERDGTYHJdefrvgbhnjmk
String
'''