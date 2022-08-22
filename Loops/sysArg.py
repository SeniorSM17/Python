import sys

print("Enter q to Exit")
for line in sys.stdin:
	if 'q' == line.rstrip():
		break
	print(f'Input : {line}')

print("Exit")
