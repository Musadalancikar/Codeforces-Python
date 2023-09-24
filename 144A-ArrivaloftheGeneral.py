

n = int(input())

height_list = list(map(int, input().split()))

x = []
y = []

for i in range(len(height_list)):
    try:
        if i == height_list.index(max(height_list), i):
            x.append(i)
    except ValueError:
        continue
    
for i in range(len(height_list)):
    try:
        if i == height_list.index(min(height_list), i):
            y.append(i)
    except ValueError:
        continue

max_index = min(x)
min_index = max(y)

if max_index < min_index:
    min_moves = abs(0-max_index) + abs(n-1-min_index)
    
else:
    min_moves = abs(0-max_index) + abs(n-1-min_index) - 1

print(min_moves)