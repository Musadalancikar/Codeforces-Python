def solve(candies):
    cnt1 = candies.count(1)
    cnt2 = candies.count(2)

    if (cnt1 + 2 * cnt2) % 2 != 0:
        return "NO"
    else:
        total_sum = (cnt1 + 2 * cnt2) // 2
        if total_sum % 2 == 0 or (total_sum % 2 == 1 and cnt1 != 0):
            return "YES"
        else:
            return "NO"

t = int(input())
total_result = []

for i in range(t):
    n = int(input())
    candies = list(map(int, input().split()))
    total_result.append(solve(candies))

for j in total_result:
    print(j)