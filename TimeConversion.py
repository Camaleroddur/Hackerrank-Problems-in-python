from sys import stdin

def main():
    time = stdin.readline().rstrip()
    time = time.split(":")
    if "PM" in time[2]:
        time[2] = time[2].replace("PM","")
        time[0] = int(time[0]) + 12
        if time[0] == 24:
            time[0] = "12"
    else:
        if time[0] == "12":
            time[0] = "00"
        time[2] = time[2].replace("AM","")
    print(str(time[0])+":"+time[1]+":"+time[2])
main()
