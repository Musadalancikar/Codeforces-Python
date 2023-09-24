
def sm_juice(juice_list):
    x = sum(juice_list)/100
    return 100 * (x/n)

n = int(input())

juice_list = list(map(int, input().split()))

print(sm_juice(juice_list))

