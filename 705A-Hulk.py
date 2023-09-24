

n = int(input())
s = 2
x = ["I", "hate", "it"]

while s <= n:    
    if s % 2 == 0:
        y = ["that", "I", "love", "it"]
        x.remove(x[-1])
        for i in y:
            x.append(i)
        s += 1
        
    else:
        z = ["that", "I", "hate", "it"]
        x.remove(x[-1])
        for i in z:
            x.append(i)
        s += 1
        
print(" ".join(x))