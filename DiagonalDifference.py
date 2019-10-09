from sys import stdin

def main():
	x = int(stdin.readline())
	mat = []
	for i in range(x):
		list1 = [int(y) for y in stdin.readline().split()]
		mat.append(list1)
	i,j,k = 0,0, len(mat)-1
	sum1 = 0
	sum2 = 0 
	while i <= len(mat) and j <= len(mat) and k >= 0:
		sum1 += mat[i][j]
		sum2 += mat[k][j]
		i += 1
		j += 1
		k -= 1
	print(abs(sum1-sum2))
main()