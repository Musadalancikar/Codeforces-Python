
n = int(input())

def yes_or_yes(strng):
    if strng.lower() == "yes":
        return "YES"
    else:
        return "NO"
    
total = []

for i in range(n):
    strng = input()
    total.append(yes_or_yes(strng))
    
for i in total:
    print(i)
    










