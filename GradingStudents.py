from sys import stdin

def main():
	x = int(stdin.readline())
	nums = []
	while x > 0:
		y = int(stdin.readline())
		nums.append(y)
		x -= 1
	num = []
	for i in range(len(nums)):
		temp = (nums[i]//5)+1
		num.append(temp)
	for i in range(len(num)):
		num[i] = num[i]*5
	final = []
	for i in range(len(nums)):
		if num[i] - nums[i] < 3 and nums[i] >= 38:
			final.append(num[i])
		else:
			final.append(nums[i])
		print(final[i])
main()
