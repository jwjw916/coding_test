import sys

input = sys.stdin.readline


while True:
    asc = input()
    if asc == "0":
        break

    if asc == asc[::-1]:
        print("yes")
    else:
        print("no")
