

k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

dragon_number = 0

for i in range(1,d+1):
    if i % k == 0:
        dragon_number += 1
    elif i % l == 0:        
        dragon_number += 1
    elif i % m == 0:
        dragon_number += 1
    elif i % n == 0:
        dragon_number += 1
    else:
        dragon_number = dragon_number
        
print(dragon_number)

