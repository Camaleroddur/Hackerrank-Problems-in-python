from sys import stdin

def main():
	list1 = [int(x) for x in stdin.readline().split()]
	list2 = [int(x) for x in stdin.readline().split()]
	a,b = 0,0
	for i in range(len(list1)):
		if list1[i] > list2[i]:
			a += 1
		if list2[i] > list1[i]:
			b += 1
	print(a,b)
main()