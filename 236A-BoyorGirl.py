def sett(string):
    x = set(string)
    if len(x) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

string = input()
print(sett(string))