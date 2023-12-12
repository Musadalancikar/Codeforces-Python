my_card = input()

table_cards = list(map(str, input().split()))

number_list = [table_cards[i][0] for i in range(5)]
color_list = [table_cards[j][1] for j in range(5)]

if my_card[0] in number_list or my_card[1] in color_list:
    print("YES")
else:
    print("NO")