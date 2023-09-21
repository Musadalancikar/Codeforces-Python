

want_matrx = [3,3]
total_matrx = []
matrx = []

for i in range(5):
    nput_matrx = list(map(int, input().split()))
    total_matrx.append(nput_matrx)
    

for i in range(len(total_matrx)):
    for j in range(len(total_matrx[i])):
        if total_matrx[i][j] > 0:
            matrx.append(i+1)
            matrx.append(j+1)
        
min_move = abs(abs(want_matrx[0] - matrx[0]) + abs(want_matrx[1] - matrx[1]))
print(min_move)