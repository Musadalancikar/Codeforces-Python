def min_square(a_b):
    min_ab = min(a_b)
    if (min_ab * 2) < max(a_b):
        return max(a_b)**2
    else:
        return (min_ab * 2)**2
        
t = int(input())
total_result = []
 
for i in range(t):
    a_b = list(map(int, input().split()))
    total_result.append(min_square(a_b))
    
for j in total_result:
    print(j)