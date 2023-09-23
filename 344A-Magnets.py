
n = int(input())

domno_list = []

for i in range(n):
    x = input()
    domno_list.append(list(x)) 


group_list = 1

for j in range(len(domno_list)-1):
    if domno_list[j][1] == "0" and domno_list[j+1][0] == "1":
        group_list = group_list

    elif domno_list[j][1] == "1" and domno_list[j+1][0] == "0":
        group_list = group_list
        
    elif domno_list[j][1] == "0" and domno_list[j+1][0] == "0":
        group_list += 1
        
    elif domno_list[j][1] == "1" and domno_list[j+1][0] == "1":
        group_list += 1
        
    else:
        group_list = group_list
        
print(group_list)
        