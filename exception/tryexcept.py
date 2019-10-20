import sys

try:
	print(int(sys.stdin.readline()))
except ValueError:
	print('Not an integer')
