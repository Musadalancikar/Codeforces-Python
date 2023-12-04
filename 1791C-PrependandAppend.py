def pre_and_app(lst):
    lst = list(lst)
    result = 0
    for j in range(int(n/2)):
        if lst[j] != lst[n-1-j]:
            result += 2
        else:
            break
    return len(lst)-result

t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = input()
    total.append(pre_and_app(lst))
    
for k in total:
    print(k)
