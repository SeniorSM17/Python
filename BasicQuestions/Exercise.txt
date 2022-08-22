#1.WAP for eligibility of a canditate voter_id, suppose age between (18 to 80 years old) using flow control conditions?
age=int(input("Entert your age"))
if age >= 18 and age <= 120:
    print("You are elegible for voting")
elif age > 120:
    print("You are not human")
else:
    print("You are not elegible for voting \n Better luck next time")
    

#2.WAP for calculating student marks in 5-subjects,and find  grades,(suppose grade A,B,C and Fail)?

marks_list=map(int,input("Enter marks of 5 subject").split())
average=sum(marks_list)/5
if average >= 90 and average<= 100:
    print("Grade - A")
elif average >= 60 and average <90:
    print("Grade - B")
elif average >= 40 and average <60:
    print("Grade- C")
else:
    print("Grade F")
    

#3.WAP for finding  even or odd number using (if .. else ... condition)?

print("Find Even or Odd")
number_even_odd= int(input("Enter the number to be check for even or odd"))
if number_even_odd % 2 == 0:
   print("Even Number")
else:
   print("Odd Number")
    
#4.WAP calculating area of a circle, result in positive integers only not in float values(hint: pi=3.14,using int() function)?

print("Area of circle")
print("Area of circle is ",int(3.14 *(int(input("Enter the radius"))**2)))

#5.WAP for finding  variables A and B are having the same memory location?

a,b= map(int,input("Enter 2 value").split())
if id(a) == id(b):
    print("Yes")
else:
    print("No")
    
""" OUTPUT 
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python 25_07_2022.py
Entert your age 16
You are not elegible for voting
 Better luck next time
Enter marks of 5 subject 20 40 50 90 80
Grade- C
Find Even or Odd
Enter the number to be check for even or odd 2222777
Odd Number
Area of circle
Enter the radius 10
Area of circle is  314
Enter 2 value 10 12
No

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task>python 25_07_2022.py
Entert your age 20
You are elegible for voting
Enter marks of 5 subject 60 70 80 90 99
Grade - B
Find Even or Odd
Enter the number to be check for even or odd 2000000000
Even Number
Area of circle
Enter the radius 7
Area of circle is  153
Enter 2 value 10 10
Yes
"""