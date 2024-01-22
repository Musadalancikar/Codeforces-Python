def replacing_elements(n, d, arr):
    if max(arr) <= d:
        return "YES"
    elif max(arr) > d:
        copy_arr = arr.copy()
        min1 = min(copy_arr)
        copy_arr.remove(min1)
        min2 = min(copy_arr)
        if min1 + min2 <= d:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
        
t = int(input())

for i in range(t):
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    print(replacing_elements(n, d, arr))