
n = int(input())

lst = list(map(int, input().split()))

ndx_lst = []

for i in range(1, n+1):
    x = lst.index(i)+1
    ndx_lst.append(str(x))
    
print(" ".join(ndx_lst))