

n = int(input())

def different_number_index(number_list):
    for i in number_list:
        if number_list.count(i) == 1:
            return number_list.index(i) + 1
            break

list1 = []

for i in range(n):
    m = int(input())
    number_list = list(map(int, input().split()))
    list1.append(different_number_index(number_list))
    
for i in list1:
    print(i)
