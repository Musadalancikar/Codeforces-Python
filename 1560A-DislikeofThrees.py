
t = int(input())

def likes_number(k):
    liks_number = []
    for i in range(1, k+1):
        a = list(str(i))
        if i % 3 == 0 or int(a[-1]) == 3:
            continue
        else:
            liks_number.append(i)
            
    return liks_number

liks_number = likes_number(1669)

number_list = []

for i in range(t):
    number_list.append(int(input()))

for j in number_list:
    print(liks_number[j-1])    

