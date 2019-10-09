from sys import stdin

def main():
	x = int(stdin.readline())
	list1 = [int(y) for y in stdin.readline().split()]
	print(sum(list1))
main()