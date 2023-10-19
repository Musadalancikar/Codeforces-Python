t = int(input())

def nmbr_list(a):
    even_list = []
    odd_list = []
    for i in range(1, a+1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
        
    return [even_list, odd_list]

even_odd_list = nmbr_list(200000)

def number(x):
    evn = even_odd_list[0][:x//2]
    odd = even_odd_list[1][:x//2]
    if int(x/2) % 2 == 0:
        odd[-1] = odd[-1] + int(x/2)
        return ["YES", evn, odd]
    else:
        return ["NO"]
        
number_list = []

for i in range(t):
    x = int(input())
    number_list.append(number(x))
    
for j in number_list:
    if j[0] == "YES":
        print(j[0])
        result = j[1] + j[2]
        print(*result)
    else:
        print(*j)
        
