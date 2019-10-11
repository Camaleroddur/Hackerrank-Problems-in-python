from sys import stdin

def main():
    s,t = [int(x) for x in stdin.readline().split()]
    a,b = [int(x) for x in stdin.readline().split()]
    app, ora = [int(x) for x in stdin.readline().split()]
    capp = [int(x) for x in stdin.readline().split()]
    cora = [int(x) for x in stdin.readline().split()]
    sum1, sum2 = 0,0
    for i in range(len(capp)):
        if a + capp[i] >= s and a + capp[i] <= t:
            sum1 += 1
    for j in range(len(cora)):
        if b + cora[j] >= s and b + cora[j] <= t:
            sum2 += 1
    print(sum1)
    print(sum2)
main()
