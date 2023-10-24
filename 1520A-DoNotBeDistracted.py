
t = int(input())

def find_all_indices(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices

total_result = []

for k in range(t):
    n = int(input())
    x = list(input())
    setx = set(x)
    total = 0
    result = []
    for i in setx:
        total_list = find_all_indices(x, i)
        if len(total_list) >= 2:
            for j in range(len(total_list)-1):
                if total_list[j+1] - total_list[j] >= 2:
                    total += 1
                else:
                    total = total 
        else:
            total = total
    
        if total >= 1:
            result.append("NO")
        else:
            result.append("YES")

    if "NO" in result:
        total_result.append("NO")
    else:
        total_result.append("YES")


for i in total_result:
    print(i)