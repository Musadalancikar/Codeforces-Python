n = int(input())
winner_list = input()

win_dan = winner_list.count("D")
win_ant = winner_list.count("A")

if win_dan > win_ant:
    print("Danik")
elif win_dan == win_ant:
    print("Friendship")
else:
    print("Anton")