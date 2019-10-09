from sys import stdin

def main():
	x = int(stdin.readline())
	list1 = [int(y) for y in stdin.readline().split()]
	suma = 0
	for i in range(x):
		suma += list1[i]
	print(suma)
main()
