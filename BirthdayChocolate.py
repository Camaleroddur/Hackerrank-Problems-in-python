from sys import stdin

def main():
	n = int(stdin.readline())
	lista = [int(x) for x in stdin.readline().split()]
	d,m = [int(x) for x in stdin.readline().split()]
	cont = 0
	for i in range(len(lista)-(m-1)):
		l = 0
		sumat = 0
		while l < m:
			sumat += lista[i+l]
			l += 1
		if sumat == d:
			cont +=1
	print(cont)
main()