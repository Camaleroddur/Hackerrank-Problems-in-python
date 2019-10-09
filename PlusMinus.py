from sys import stdin

def main():
    x = int(stdin.readline())
    list1 = [int(y) for y in stdin.readline().split()]
    neg,pos,ze = [],[],[]
    for i in range(len(list1)):
        if list1[i] < 0:
            neg.append(list1[i])
        elif list1[i] > 0:
            pos.append(list1[i])
        else:
            ze.append(list1[0])
    neg1,pos1,ze1 = len(neg)/x,len(pos)/x,len(ze)/x
    print("%.6f" % pos1)
    print("%.6f" % neg1)
    print("%.6f" % ze1)
main()
