from sys import stdin

def main():
    list1 = [int(x) for x in stdin.readline().split()]
    p = 0
    r = len(list1)
    sumlist = []
    while r > 0:
        sum1 = 0
        for i in range(len(list1)):
            if i == p:
                pass
            else:
                sum1 += list1[i]
        r -= 1
        p += 1
        sumlist.append(sum1)
    sumlist.sort()
    print(sumlist[0],sumlist[len(sumlist)-1])
main()
