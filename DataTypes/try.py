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