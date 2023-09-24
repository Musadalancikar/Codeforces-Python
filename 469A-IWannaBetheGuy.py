
n = int(input())

x_list = list(map(int, input().split()))
y_list = list(map(int, input().split()))

x_level = x_list[1:]
y_level = y_list[1:]

total = 0

for i in range(1,n+1):
    if i not in x_level and i not in y_level:
        total += 1

if total == 0:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
    

