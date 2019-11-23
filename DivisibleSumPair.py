from sys import stdin

def main():
	n, k = [int(x) for x in stdin.readline().split()]
	lista = [int(x) for x in stdin.readline().split()]
	cont = 0
	for i in range(len(lista)-1):
		for j in range(i+1,len(lista)):
			suma = 0
			suma = lista[i] + lista[j]
			if suma % k == 0:
				cont += 1
	print(cont)
main()