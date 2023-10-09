
n, k, l, c, d, p, nl, np = list(map(int, input().split()))

total_ml = k * l
                                
max_limes = c * d

process1 = int(total_ml / nl)
process2 = max_limes
process3 = int(p / np)



def min_total(process1, process2, process3):
    return int(min(process1, process2, process3) / n)

print(min_total(process1, process2, process3))                             
