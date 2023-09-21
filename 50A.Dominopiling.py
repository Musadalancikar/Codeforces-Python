import math

i_npt = input().split()
M = int(i_npt[0])
N = int(i_npt[1])

if 1<= M <= N <= 16:
    alan= M * N
    dominoalan = 2 * 1
    
    maxalan = alan / dominoalan
    
    alt_taban = math.floor(maxalan)
    
    print(alt_taban)
    
    