
n = int(input())

easy_or_hard_list = list(map(int, input().split()))

if 1 in easy_or_hard_list:
    print("HARD")
else:
    print("EASY")