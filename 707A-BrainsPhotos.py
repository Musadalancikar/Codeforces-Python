def photos(photos_list):
    sayac = 0
    for j in photos_list:
        if "C" in j:
            sayac += 1
        elif "M" in j:
            sayac += 1
        elif "Y" in j:
            sayac += 1
            
    if sayac == 0:
        return "#Black&White"
    else:
        return "#Color"
        
t = list(map(int, input().split()))
photos_list = []

for i in range(t[0]):
    photos_list.append(list(map(str, input().split())))

print(photos(photos_list))
    