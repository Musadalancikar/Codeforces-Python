w = int(input())

if (1 <= w <= 100):
    if (w % 2 == 0):
        if w == 2:
            print("No")
        else:
            print("Yes")
        
    else:
        print("No")
else:
    print("No")