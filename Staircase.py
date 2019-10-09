from sys import stdin

def main():
	x = int(stdin.readline())	
	for i in range(1,x+1):
		print((" "*(x-i))+("#"*i))
main()
