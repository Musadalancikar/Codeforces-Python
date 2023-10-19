

t = int(input())

def timur(marathon_list):
    timr = marathon_list[0]
    total = 0
    for i in marathon_list:
        if timr < i:
            total += 1
        else:
            total = total
    return total
    
result = []

for i in range(t):
    marathon_list = list(map(int, input().split()))
    result.append(timur(marathon_list))

for j in result:
    print(j)
    
    