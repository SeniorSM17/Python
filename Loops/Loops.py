#!/usr/bin/env python
# coding: utf-8

# ## Exercise Patterns
1. Write a program to print the following Patterns

  1 2 3 4 5 
  1 2 3 4 5  
  1 2 3 4 5 
  1 2 3 4 5 
  1 2 3 4 5
# In[8]:


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,number+1):
        print(columns," ",end="")
    print("")

2.Write a program to print the following Pattern

  5 4 3 2 1 
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1
  5 4 3 2 1 
# In[9]:


number=int(input("Enter the number"))
for rows in range(number,0,-1):
    for columns in range(number,0,-1):
        print(columns," ",end="")
    print("")

3.Write a program to print the following Pattern
  5 5 5 5 5 
  4 4 4 4 4 
  3 3 3 3 3 
  2 2 2 2 2 
  1 1 1 1 1
# In[18]:


number=int(input("Enter the number"))
temp=number
for rows in range(number,0,-1):
    for columns in range(number,0,-1):
        print(temp ," ",end="")
    temp=temp-1
    print("")

4. Write a program to print the following Pattern
  1
  1 2
  1 2 3
  1 2 3 4
  1 2 3 4 5
# In[24]:


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,rows+1):
        print(columns ," ",end="")
    print("")

5.Write a program to print the following Pattern
  1 
  2 2 
  3 3 3 
  4 4 4 4 
  5 5 5 5 5
# In[21]:


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(rows ," ",end="")
    print("")

6.Write a program to print the following Pattern
  1 
  2 3  
  4 5 6 
  7 8 9 10 
  11 12 13 14 15
# In[25]:


number=int(input("Enter the number"))
temp=1
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(temp ," ",end="")
        temp+=1
    print("")

7.Write a program to print the following Pattern
  5 
  4 4 
  3 3 3 
  2 2 2 2 
  1 1 1 1 1
# In[37]:


number=int(input("Enter the number"))
temp=number
for rows in range(0,number):
    for columns in range(0,rows+1):
        print(temp ," ",end="")
    temp-=1
    print("")

8.Write a program to print the following Pattern
  1 
  2 3 
  3 4 5 
  4 5 6 7 
  5 6 7 8 9
# In[50]:


number=int(input("Enter the number"))
for rows in range(1,number+1):
    temp=rows
    for columns in range(0,rows):
        print(temp ," ",end="")
        temp+=1
    print("")

9.Write a program to print the following Pattern
  A 
  B C
  D E F
  G H I J
  K L M N O
# In[63]:


number=int(input("Enter the number"))
temp=65
for rows in range(1,number+1):
    for columns in range(0,rows):
        print(chr(temp)," ",end="")
        temp+=1
    print("")

10.Write a program to print the following Pattern
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
   * * * * * 
# In[64]:


number=int(input("Enter the number"))
for rows in range(number,0,-1):
    for columns in range(number,0,-1):
        print("*"," ",end="")
    print("")

11.Write a program to print the following Pattern
   * 
   * * 
   * * * 
   * * * * 
   * * * * * 
# In[65]:


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,rows+1):
        print("*" ," ",end="")
    print("")

12.Write a program to print the following Pattern
    * * * * * 
    *       * 
    *       * 
    *       * 
    * * * * * 
# In[86]:


number=int(input("Enter the number"))
for rows in range(1,number+1):
    for columns in range(1,number+1):
        if rows == 1 or rows == number:
            print("*"," ",end="")
        elif columns ==1 or columns == number:
             print("*"," ",end="")
        else:
            print("  ",end=" ")
    print("")


# In[87]:


number=int(input("Enter the number"))
k = 0
for i in range(1, number+1):
    for space in range(1, (number-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ", end="")
        k += 1
   
    k = 0
    print()

14.Display Multiplication Table in given range using Nested for loop
# In[93]:


for rows in range(1,11):
       for columns in range(1,11):
           print(rows*columns," ",end="")
       print("")

15.Display Prime Numbers in the given range using nested for loops 
# In[95]:


print("List of prime numbers from 1 to 100 :")
for n in range (1, 101):
    count = 0
    t = n//2
    for i in range(2, (t + 1)):
        if(n % i == 0):
            count = count + 1
            break
    if (count == 0 and n > 1):
        print(" %d" %n, end = '  ')

#Doubt
16.Write a program to print the following Pattern
                 1
              3  2
          6   5  4
      10  9   8  7#Doubt
m = int(input())
n = int(input())
k = m
for i in range(1, n+1):
    for j in range(1, (n - i)+1):
        print(" ", end = " ")
    for j in range(1, i+1):
        print(k, end = " ")
        k +=1
    print()
17.Write a program to print the following Pattern
10  9  8   7
      6   5  4
           3  2
               1
# In[57]:


t=10
s=0
for i in range(4,0,-1):
    print(' '*s**2,end=' ')
    for j in range(1,i+1):
        print(t,end=' ')
        t-=1
    s=s+1
    print()

18 Accept 10 numbers from the user and display their average. 
# In[130]:


list_number=list(map(int,input().split()))
print("Average of enterted number is : ", sum(list_number)/10)


# In[131]:


print("Please Enter 10 number")
list_num =[]
sums=0
for i in range(10):
    sums+= int(input())
print("Average of enterted number is : ", sums/10)
    


# ## Exeercise -> Loop
Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers) 
# In[54]:


sums=0
sums1=0
for i in range(12,38):
    if i%2!=0:
        sums+=i
    else:
        sums1+=i
print(sums,sums1)

Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500. 
# In[134]:


for i in range(100,500):
    if i %11==0 and i%2!=0:
        print(i,end=",")

Write a program to print numbers from 1 to 20 except multiple of 2 & 3 
# In[136]:


for i in range(1,21):
    if i%2==0 or i%3==0:
        pass
    else:
        print(i,end=",")

Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers. 
# In[137]:


num=1
i=-1
s=0
while(num!=0):
    num=int(input("Enter any number"))
    s=s+num
    i=i+1
print("Average",s/i)

Write a program to accept decimal number and display its binary number. 
# In[16]:


number=int(input("Enter the decimal number"))
binary_number=0
while number >0:
    binary_number = binary_number * 10 +number%2
    number=number//2
print(binary_number)

Convert the following loop into for loop : 

x = 4 

while(x<=8): 

    print(x*10) 

    x+=2 
# In[20]:


for i in range(4,9,2):
    print(i*10)

What is nested loop? 

A nested loop is a loop within a loop, an inner loop within the body of an outer one.
Write a program to convert temperature in Fahrenheit to Celsius. 
# In[24]:


temperature=float(input("Enter the temperature in Fahrenheit"))
print("The temperature in degree Celsisus is ", round((temperature -32)*(5/9),2))


# In[26]:


nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence:")
    while count < nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1

Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz". 
# In[28]:


for i in range(0,51):
    if i % 3==0 and i %5==0 :
        print("FizzBuzz", end = " ,")
    elif i%3==0:
        print("Fizz",end=" ,")
    elif  i%5==0:
        print("Buzz",end=" ,")
    else:
        print(i,end=" ,")

Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 

Note : Use 'continue' statement. 

Expected Output : 0 1 2 4 5 
# In[30]:


for i in range(0,7):
    if i == 3 or i == 6:
        continue
    else:
        print(i,end=", ")


# # Exercise -> Team 
Write a program to get all vowels from given string
# In[32]:


str1=input("Enter a string")
vowels=["a","e","i","o","u"]
for i in str1.lower():
    if i in vowels:
        print(i,end=", ")

Write a program to calculate the simple interest
# In[33]:


principle = float(input("Enter the Princliple amount"))
rate=float(input("Enter the rate of simple intrest"))
time=int(input("Enter the period \nNote enter period in integer format only"))
print("The intrest is ",(principle*rate*time)/100)

Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N
# In[34]:


n=int(input("Enter the number of terms: "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+(1/i)
print("The sum of series is",round(sum1,2))

Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
# In[35]:


def sumOfSeries(num): 
    res = 0
    fact = 1
       
    for i in range(1, num+1): 
        fact *= i 
        res = res + (i/ fact) 
           
    return res 
       
n=int(input("Enter the number of terms: "))
 
print("Sum: ", sumOfSeries(n)) 

Python Program to Replace All Occurrences of ‘a’ with $ in a String
# In[38]:


str1= input("Enter the string")
str2=""
for i in str1.lower():
    if i =='a':
        str2+='$'
    else:
        str2+=i
print(str2)


# # Problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

 

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

https://leetcode.com/problems/two-sum/
# In[52]:


target=int(input("Enter the target number"))
list_num=list(map(int,input("ENter the lsit of number").split()))
ls_index=[]
for i in range(len(list_num)):
    for j in range(i,len(list_num)):
        if i==j:
            continue
        elif list_num[i]+list_num[j] == target:
            ls_index.append((i,j))
print(ls_index,end=" ")


# In[ ]:




