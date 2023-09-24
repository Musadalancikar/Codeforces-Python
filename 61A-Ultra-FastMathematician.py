

n = list(map(int, input()))
k = list(map(int, input()))

result = []

for i in range(len(n)):
    if n[i] + k[i] == 1:
        result.append("1")
    else:
        result.append("0")
        
print("".join(result))

