t = int(input())
result = []

for i in range(t):
    n = int(input())
    lst = list(map(str, input().split()))
    lst = "".join(lst)
    lst = lst.split("1")
    len_list = [len(i) for i in lst]
    result.append(max(len_list))
    
for j in result:
    print(j)