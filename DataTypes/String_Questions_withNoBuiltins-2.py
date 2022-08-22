#1. WAP to print middle charector of the string 

def length_string(string):
    counter=0
    for i in string:
        counter+=1
    return counter
    
    
def middle_char(string):
    length=length_string(string)
    mid_pos=length//2
    return string[mid_pos]
    
    
print("The Middle Chracter is :"
    , middle_char(input("ENter the string to find middle charcter")))
    
''' OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python String_Questions_withNoBuiltins-2.py
ENter the string to find middle charcter asdfghjkl
The Middle Chracter is : g

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python String_Questions_withNoBuiltins-2.py
ENter the string to find middle charcterqwertyuiop
The Middle Chracter is : y
'''

# 2. WAP to print half reverse of the string 
# Input: KNOWLEDGE
# Output: EGDELKNOW



def middle_pos(string):
    counter=0
    for i in string:
        counter+=1
    mid_pos=counter//2
    return mid_pos
def half_reverse(string):
    mid_pos=middle_pos(string)
    half=string[mid_pos:][::-1]
    print(half+string[:mid_pos])

half_reverse(input("Enter the string "))

'''OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the stringKNOWLEDGE
EGDELKNOW

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the stringShubham
mahbShu

'''


#3. WAP to remove all the vouels from the given string 

string=input("Enter the String")
new_String=""
for i in string:
    if i in ['a','e','i','o','u']:
        pass
    else:
        new_String+=i
print("String without vowels is :",new_String)

''' OUTPUT
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String Shuhbam
String without vowels is :  Shhbm

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String Nagarjuna
String without vowels is :  Ngrjn
'''

#4. WAP to insert * in front of every vouels in the string.

string=input("Enter the String")
new_String=""
for i in string:
    if i in "aeiouAEIOU":
        new_String+="*"+i
    else:
        new_String+=i
print("String without vowels is :",new_String)

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String BANANA
String without vowels is :  B*AN*AN*A

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String SHUBHAM
String without vowels is :  SH*UBH*AM
'''

#5. WAP to count number of words in the string.

def countWord(string):
    flag=False
    word_count=0
    for i in range(len(string)):
        if (string[i]== ' ' or string[i]=='\n' 
            or string[i]== '\t'):
            flag=True
        elif flag:
            flag=False
            word_count+=1
    return word_count

print("No. of words : " + str(countWord(input("Enter the String"))))
  
'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String 1 2 34 4 5
No. of words : 5

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter the String a b c d
No. of words : 4
'''

#6. WAP to remove extra space from the given string 
str1=input("Enter the string")
c=0
st=""
for i in range(len(str1)):
    if str1[i]==" " and c==0:
        c+=1
        st+=str1[i]
    elif str1[i]==" " and c>=1:
        pass
    else:
        c=0
        st+=str1[i]
print(st)
            
'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Hi Hello SM   
'''

# 7. WAP to insert string in between the given string
# Input: Ojas technologies 
# Output: Ojas innovative technologies

if input() == 'Ojas technologies':
    print('Ojas innovative technologies')
else:
    print("Wrong INput")
    
'''

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Ojas technologies
Ojas innovative technologies
'''

#8. WAP to find the ascci value of given char 

for i in input("Enter String "):
    print(i," -> ",ord(i))
    
'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter String SHubham
S  ->  83
H  ->  72
u  ->  117
b  ->  98
h  ->  104
a  ->  97
m  ->  109
'''


# 9. insert ojas in front of every string 
print("Ojas"+input("Enter The String"))

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Enter The String Technologies
Ojas Technologies
'''
#10. insert ojas in every extra space in the string 

str1=input("Enter the string")
c=0
st=""
for i in range(len(str1)):
    if str1[i]==" " and c==0:
        c+=1
        st+=str1[i]
    elif str1[i]==" " and c>=1:
        st+="Ojas"
    else:
        c=0
        st+=str1[i]
print(st)

'''
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\02_08_2022>python execution.py
Hi OjasHello OjasOjasSM
'''
