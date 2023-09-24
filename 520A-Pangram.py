
n = int(input())

string = input()

alfabe = "abcdefghijklmnopqrstuvwxyz"
string = set(string.lower())

x = 0

for i in string:
    if i not in alfabe:
        x += 1
    else:
        x = x
        
if x == 0:
    if len(alfabe) == len(string):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
