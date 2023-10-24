

a_list = list(map(int, input().split()))

s = list(input())

total = 0

for i in range(len(s)):
    total += a_list[int(s[int(i)])-1]
    
print(total)