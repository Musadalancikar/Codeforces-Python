def two_array(a, b):
    swap = 0
    while swap < k:
        a_min = a.index(min(a))
        swapped = False
        for j in range(len(a)):
            if a[a_min] < max(b):
                a[a_min] = max(b)
                b.remove(max(b))
                swap += 1
                swapped = True
            if swap >= k:
                break
        if not swapped:
            break
    return sum(a)

t = int(input())
total_result = []

for i in range(t):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))        
    b = list(map(int, input().split()))        
    total_result.append(two_array(a, b))

for k in total_result:
    print(k)