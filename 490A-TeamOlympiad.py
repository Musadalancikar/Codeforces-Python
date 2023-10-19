n = int(input())

k = list(map(int, input().split()))

wanted_element = [1, 2, 3]

y = []

for element in wanted_element:
    indexs = [i+1 for i, x in enumerate(k) if x == element]
    y.append(indexs)


a = len(y[0])
b = len(y[1])
c = len(y[2])

total = []
result = 0

for i in range(min(a, b, c)):
    if a >= 1 and b >= 1 and c >= 1:
        total.append([y[0][0], y[1][0], y[2][0]])
        y[0].remove(y[0][0])
        y[1].remove(y[1][0])
        y[2].remove(y[2][0])
        result += 1
        
    else:
        break
    
print(result)
for i in total:
    print(*i)
