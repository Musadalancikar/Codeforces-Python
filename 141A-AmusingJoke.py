

guest_name = input()
residence_name = input()
door_in_the_morning_name = input()

total_name = guest_name + residence_name
set_name = set(total_name)
set_door_name = set(door_in_the_morning_name)


total = 0

if len(set_name.difference(set_door_name)) >= 1:
    total += 1
elif len(set_door_name.difference(set_name)) >= 1:
    total += 1
else:
    for i in set_name:
        if i in total_name and i in door_in_the_morning_name:
            if total_name.count(i) == door_in_the_morning_name.count(i):
                total = total
            else:
                total += 1
                break
        elif i in total_name and i not in door_in_the_morning_name:
            total += 1
            break
        else:
            total = total
            

if total == 0:
    print("YES")
else:
    print("NO")
