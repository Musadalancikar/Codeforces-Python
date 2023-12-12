def stone_game1(n, lst):
    lst_copy = lst.copy()
    min_lst = min(lst_copy)
    max_lst = max(lst_copy)
    total = 0
    for j in range(n):
        if min_lst in lst_copy or max_lst in lst_copy:
            lst_copy.remove(lst_copy[0])
            total += 1
        else:
            break
    return total

def stone_game2(n, lst):
    lst_copy = lst.copy()
    min_lst = min(lst_copy)
    max_lst = max(lst_copy)
    total = 0
    for j in range(n):
        if min_lst in lst_copy or max_lst in lst_copy:
            lst_copy.remove(lst_copy[-1])
            total += 1
        else:
            break
    return total

def stone_game3(n, lst):
    lst_copy = lst.copy()
    min_lst = min(lst_copy)
    max_lst = max(lst_copy)
    total = 0
    for j in range(n):
        if min_lst in lst_copy:
            lst_copy.remove(lst_copy[0])
            total += 1
        else:
            break
    if max_lst in lst_copy:
        for k in range(len(lst_copy)):
            if max_lst in lst_copy:
                lst_copy.remove(lst_copy[-1])
                total += 1
            else:
                break
    return total

def stone_game4(n, lst):
    lst_copy = lst.copy()
    min_lst = min(lst_copy)
    max_lst = max(lst_copy)
    total = 0
    for j in range(n):
        if min_lst in lst_copy:
            lst_copy.remove(lst_copy[-1])
            total += 1
        else:
            break
    if max_lst in lst_copy:
        for k in range(len(lst_copy)):
            if max_lst in lst_copy:
                lst_copy.remove(lst_copy[0])
                total += 1
            else:
                break
    return total

t = int(input())
result = []

for i in range(t):
    result1 = []
    n = int(input())
    lst = list(map(int, input().split()))
    result1.append(stone_game1(n, lst))
    result1.append(stone_game2(n, lst))
    result1.append(stone_game3(n, lst))
    result1.append(stone_game4(n, lst))
    result.append(min(result1))
    
for k in result:
    print(k)