

year = int(input())

year_min = year + 1

while year < year_min:    
    if len(set(str(year_min))) == len(str(year)):
        print(year_min)
        break
    else:
        year_min += 1


