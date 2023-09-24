
def color_list(c_list):
    x = set(c_list)
    return len(c_list) - len(x)

c_list = list(map(int, input().split()))

print(color_list(c_list))