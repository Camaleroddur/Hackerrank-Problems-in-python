from sys import stdin

def main():
    year = int(stdin.readline())
    if year >= 1700 and year <= 1917:
        if year % 4 == 0:
            print("12.09."+str(year))
        else:
            print("13.09."+str(year))
    elif year == 1918:
        print("26.09."+str(year))
    else:
        if year % 400 == 0 or (year % 4 == 0 and  year % 100 != 0):
            print("12.09."+str(year))
        else:
            print("13.09."+str(year))
main()
