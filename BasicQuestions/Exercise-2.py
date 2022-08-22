#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?


list_numbers=list(map(int,input("Enter the number").split()))
targer_value=int(input("Entert the Target Value"))
if targer_value in list_numbers:
    print(targer_value," is present in list")
else:
    print(targer_value," is absent in list")
  
  
''' OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\01_08_2022>python 01_08_2022.py
Enter the number 1 5 3 4 6 7 890 90
Entert the Target Value 5
5  is present in list

'''

#2. WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?
list1 = [1,5,7,8,90,6,23]
for i in range(len(list1)):
    for j in range(i+1,len(list1)):
        if list1[i]>list1[j]:
            list1[i], list1[j] = list1[j], list1[i]
print("Sorted list: ", list1)


#output
Sorted list:  [1, 5, 6, 7, 8, 23, 90]

            
#============================================================================================================================================

#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and rate of return is 5 percentage for annum.
#  and display the total amount to pay on  the end of the year.?
#formula is A= p *((1+r/100))**time

principal_amount = int(input("Enter Principal: "))
time_period = int(input("Enter years: "))
rate_of_interest = int(input("Enter rate: "))
ONE_CONSTANT = 1
amount = principal_amount*(ONE_CONSTANT+rate_of_interest/100)**time_period
#print(compound_interest_constant)
#amount = principal_amount*compound_interest_constant

print("Total amount is ", int(amount))

#output
Enter Principal: 10000
Enter years: 3
Enter rate: 5
1.1576250000000001
Total amount is  11576

#==========================================================================================================================================
'''
'''
#4. WAP to calculate the sum of the given matrix   [[x1,x2,x3],[x4,x5,x6],[x7,x8,x9]], where x1,x2....x9 values must take from command-line
#   arguments?
""" 1 2 3
    4 5 6  
    7 8 9   

sum is : 45   """

ls = []
for i in range(3):
    ls1=[]
    for j in range(3):
        ls1.append(int(input()))
    ls.append(ls1)    
print(ls)
sums = 0
for i in range(3):
    for j in range(0,len(ls[i])):
        #print(ls[i])
        sums+=ls[i][j]
print(sums) 

#0utput
1
2
3
4
5
6
7
8
9
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
45       



#=============================================================================================================================================

#5. WAP pattern program

"""  * * * * *
      * * * *
       * * *
        * *
         *
        * *
       * * *
      * * * * 
     * * * * *     """
n = int(input())
for i in range (0, n):
    spaces = " " * i
    stars = "* " * (n - i)
    print(spaces + stars)
k = n -1
for j in range(2, k+1):
    spaces = " " * (n - j)
    stars = "* " * (j)
    print(spaces + stars)
print("* " * n)


#output
5
* * * * *
 * * * *
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
'''