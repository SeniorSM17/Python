#1. How would you confirm that 2 strings have the same identity?
st2=input("Enter the string: ")
st1=st2
if st1 is st2:
    print("same identity")

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the string: a
same identity
'''

#2. How would you check if each word in a string begins with a capital letter?

st1=input("Enter the string: ")
ls=list(st1.split(" "))
c=0
for i in ls:
    if i[0].isupper():
        c+=1
    else:
        c=0
if len(ls) == c:
    print("each word in a string begins with a capital letter")
else:
    print("each word in a string DOES NOT begins with a capital letter")
   
'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the string: Abhbhdbf Abhhbdhb Anhjbhdbf
each word in a string begins with a capital letter

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the string: jashda AJHDJSH ksjdjadjAkj kljkjAk Akjkljkjsd
each word in a string DOES NOT begins with a capital letter
'''

#3. Check if a string contains a specific substring
st1= input("Enter the String").strip()
sub_string=input("Enter the Substring").strip()

if sub_string.lower() in st1.lower():
    print("Yes Substring is Present")
else:
    print("No Substring is not present")
    
'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String ABCD
Enter the Substring cd
Yes Substring is Present

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String ASDFGHJKL
Enter the Substring DFGH
Yes Substring is Present
'''

#4. Find the index of the first occurrence of a substring in a string

st1= input("Enter the String").strip()
sub_string=input("Enter the Substring").strip()

if st1.find(sub_string) !=-1:
    print('Found at position: ',st1.find(sub_string))
else:
    print("Not in String")
    
'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String Hello my name is SM
Enter the Substring SM
Found at position:  17
'''


#5. Count the total number of characters in a string

print(len(input("Enter the String").strip()))
cd 

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String sdfg gh hjk
11
'''
#6. Count the number of a specific character in a string
print(input("Enter the String ").strip().count(input("Enter the Character ").strip()))

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the Stringasdasdasdasdf
Enter the Character a
4
'''

#7. Capitalize the first character of a string
print(input("Enter the String ").strip().capitalize())

#8. What is an f-string and how do you use it?

# Using f-strings is similar to using format().
# F-strings are denoted by an f before the opening quote.

name=input("Enter the name ")
company=input("Enter the name of company ")
print(f'Hi my name is {name} and work in {company}')

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the name SM
Enter the name of company Ojas
Hi my name is  SM and work in  Ojas
'''

#9. Search a specific part of a string for a substring
