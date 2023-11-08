def max_gcd(gcd):
    if gcd % 2 == 0:
        return int(gcd / 2)
    else:
        return int((gcd-1)/2)

t = int(input())

total_result = []

for i in range(t):
    gcd = int(input())
    total_result.append(max_gcd(gcd))

for l in total_result:
    print(l)    

