
n = int(input())

capasity_list = []
for i in range(n):
    ext, entr = list(map(int, input().split()))
    capasity_list.append([ext,entr])
    
total_capasity = 0
max_capasity = []
for j in capasity_list:
    total_capasity -= j[0]
    total_capasity += j[1]
    max_capasity.append(total_capasity)
    
print(max(max_capasity))