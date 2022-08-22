#!/usr/bin/env python
# coding: utf-8

# # Problem statement
# Python Program to accept three distinct digits and print all possible combinations from the digits.

Case 1:
Enter first number:1
Enter second number:2
Enter third number:3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

Case 2:
Enter first number:5
Enter second number:7
Enter third number:3
5 7 3
5 3 7
7 5 3
7 3 5
3 5 7
3 7 5
# In[25]:


arr=list(map(int,input("Enter 3 numbers").split()))
from itertools import permutations
for d in permutations(arr):
    print(d,end=",")


# # Exercise Team 3

Q1.WAP in python arrange string characters such that lowercase letters should come first
Q2.WAP to print sum of prime numbers in given list input :- 2 4 5 6 7 3 8 output :- 17
Q3.when do we use nested for loop.Write an example.
Q4.WAP in python remove all characters from a string except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )
Q5.WAP to take a list and find the possition of the item .(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)
# In[30]:


str1=input("ENter the string ")
upper=""
lower=""
for i in str1:
    if i.islower():
        lower+=i
    else:
        upper+=i
print(lower+upper)


# In[78]:





# In[84]:


def isprime(number):
    flag=True
    for i in range(2,number):
        if number%i==0:
            flag=False
    return flag

ls=list(map(int,input("Enter the numbers").split()))
sums=0
for i in ls:
    if isprime(i):
        sums+=i
print(sums)

Q3.when do we use nested for loop.Write an example.
If a loop exists inside the body of another loop, it's called a nested loop. Here's an example of the nested for loop.

// outer loop
for (int i = 1; i <= 5; ++i) {
  // codes

  // inner loop
  for(int j = 1; j <=2; ++j) {
    // codes
  }
..
}Q4.WAP in python remove all characters from a string except integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )
# In[88]:


str1=input("Enter the number ")
op=""
for i in str1:
    od= ord(i)
    if od >= 48 and od <=57:
        op+=i
print(op)


# In[91]:


ls1=list(map(int,input("Enter the list").split()))
num= int(input("Enter the number"))
print("Index position is ",ls1.index(num))


# In[ ]:




