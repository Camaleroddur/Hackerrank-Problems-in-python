from sys import stdin

def main():
	x = int(stdin.readline())
	list1 = [int(y) for y in stdin.readline().split()]
	list1.sort()
	maxi = list1[len(list1)-1]
	cant = 0
	for i in range(len(list1)-1,-1,-1):
		if list1[i] == maxi:
			cant += 1
	print(cant)
main()