

n = list(map(int, input().split()))
lst = list(map(int, input().split()))

sayac = 0

if n[0] == len(lst):
    nmb = lst[n[1]-1]
    if max(lst) == 0:
        sayac = 0
    else:
        for i in lst:
            if i > 0:
                if nmb <= i:
                    sayac += 1
                else:
                    sayac = sayac

print(sayac)
