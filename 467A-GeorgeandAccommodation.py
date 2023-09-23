

n = int(input()) 

room_list = []

for i in range(n):
    r_capasty, f_capasty = list(map(int, input().split()))
    room_list.append([r_capasty, f_capasty])

friens_room = 0

for j in room_list:
    if j[1] - j[0] >= 2:
        friens_room += 1
    else:
        friens_room = friens_room
        
print(friens_room)