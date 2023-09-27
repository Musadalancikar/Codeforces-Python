

x = list(input())
x.remove(x[0])
x.remove(x[-1])

alfabe = "abcdefghijklmnopqrstuvwyzx"

y = set(x)

total = 0

for i in y:
    if i in alfabe:
        total += 1
    else:
        total = total
        
print(total)