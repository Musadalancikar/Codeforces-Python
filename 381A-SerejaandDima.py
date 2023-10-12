

n = int(input())

number_list = list(map(int, input().split()))

def total_game_score(number_list):
    sereja_total = 0
    dima_total = 0
    total = 1
    
    for i in range(n):
        if total % 2 != 0:
            if number_list[0] > number_list[-1]:
                sereja_total += number_list[0]
                number_list.remove(number_list[0])
                total += 1
            else:
                sereja_total += number_list[-1]
                number_list.remove(number_list[-1])
                total += 1
        else:
            if number_list[0] > number_list[-1]:
                dima_total += number_list[0]
                number_list.remove(number_list[0])
                total += 1
            else:
                dima_total += number_list[-1]
                number_list.remove(number_list[-1])
                total += 1

    return f"{sereja_total} {dima_total}"
    
print(total_game_score(number_list))