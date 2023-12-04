def triple(arr):   
    count_dict = {}

    ans = -1
    
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1

        if count_dict[num] >= 3:
            ans = num
            break

    return ans

t = int(input())  
total = []

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    total.append(triple(arr))
    
for j in total:
    print(j)


