def sequence(n, lst):
    if n % 2 == 1:
        first_lst = lst[:int((n + 1)/2)]
        second_lst = lst[int((n + 1)/2):]
        second_lst = second_lst[::-1]
        result = []
        for j in range(len(second_lst)):
            result.append(first_lst[j])
            result.append(second_lst[j])
        result.append(first_lst[-1])
        return result
        
    else:
        result = []
        first_lst = lst[:int(n/2)]
        second_lst = lst[int(n/2):]
        second_lst = second_lst[::-1]
        for j in range(len(second_lst)):
            result.append(first_lst[j])
            result.append(second_lst[j])
        return result
    
t = int(input())
total = []

for i in range(t):
    n = int(input())
    lst = list(map(int, input().split()))
    total.append(sequence(n, lst))

for k in total:
    print(*k)