
n = int(input())
k = [1,2,3,4,5,6,7,8,9,10]
total_list = []

def total_(A, B):
    dif = abs(A-B)
    a = 0
    total = 0
    if dif > 0:
        while dif > 0:
            if dif // k[-1-a] > 0:
                total += (dif // k[-1-a])
                dif = abs(dif- ((dif // k[-1-a]) * (k[-1-a])))
            else:
                a += 1
    return total

for i in range(n):
    A, B = list(map(int, input().split()))
    total_1 = total_(A, B)
    total_list.append(total_1)
    
for i in total_list:
    print(i)
    


