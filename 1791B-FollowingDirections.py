def sugar(move):
    sugar_move = [0, 0]
    while True:
        for j in move:
            if j == "U":
                sugar_move[1] += 1
                if sugar_move == [1, 1]:
                    return "YES"
                
            elif j == "D":
                sugar_move[1] -= 1
                if sugar_move == [1, 1]:
                    return "YES"
                
            elif j == "R":
                sugar_move[0] += 1
                if sugar_move == [1, 1]:
                    return "YES"
                
            elif j == "L":
                sugar_move[0] -= 1
                if sugar_move == [1, 1]:
                    return "YES"
        else:
            return "NO"
        
t = int(input())
total = []

for i in range(t):
    n = int(input())
    move = input()
    total.append(sugar(move))

for k in total:
    print(k)    