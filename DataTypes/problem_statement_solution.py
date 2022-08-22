n = int(input())
student_marks = {}
for _ in range(n):
	name, *line = input().split()
	scores = list(map(float, line))
	scores=sum(scores)/3
	student_marks[name] = scores
query_name = input()
print('%.2f' % student_marks[query_name])

''' OUTPUT
Input (stdin)

Download
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Expected Output

Download
56.00

Compiler Message
Success
Input (stdin)

Download
2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Expected Output

Download
26.50
'''