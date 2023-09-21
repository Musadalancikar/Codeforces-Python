a = input()
b = input()

x = a.lower()
y = b.lower()

lst = [x,y]
lst1 = sorted(lst)

if x == y:
    print(0)
else:
    if x == lst1[0] and y == lst1[1]:
        print(-1)
    elif x == lst1[1] and y == lst1[0]:
        print(1)
    