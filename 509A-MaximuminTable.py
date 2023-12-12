n = int(input())

empty_matrix = [[1] * n for _ in range(n)]

for i in range(n-1):
    for j in range(n-1):
        empty_matrix[i+1][j+1] = empty_matrix[i][j+1] + empty_matrix[i+1][j] 

max_table = max(max(empty_matrix))        
print(max_table)