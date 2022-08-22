#Problem Statement

'''
Problem statement
------------------

You are required to enter a word that consists of x and y 
that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 * x = y


Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

    First line: A word that starts with several Zs and continues by several Os.
    Note: The maximum length of this word must be 20.

    

Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

instruction
-----------
if input = zzzoooooo then print "yes".
if input = zzooo print "no"
'''


word=input()
if word.count('z')*2 == word.count("o"):
	print("Yes")
else:
	print("No")
    
(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\01_08_2022>python Problem_statement_solution.py
zzoooo
Yes

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\01_08_2022>python Problem_statement_solution.py
zzzoooooo
Yes

(base) C:\Users\sm22227\Documents\Shubham\Python\Office Task\01_08_2022>python Problem_statement_solution.py
zzooo
No