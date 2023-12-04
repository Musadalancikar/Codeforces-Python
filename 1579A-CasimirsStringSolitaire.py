def string_solitaire(string):
    lst = list(string)
    if len(string) % 2 == 1:
        return "NO"
    else:
        for j in range(len(lst)):
            if "A" in lst and "B" in lst:
                lst.remove("A")
                lst.remove("B")
            elif "B" in lst and "C" in lst:
                lst.remove("B")
                lst.remove("C")
            else:
                if len(lst) == 0:
                    return "YES"
                else:
                    return "NO"
            
t = int(input())
total = []

for i in range(t):
    string = input()
    total.append(string_solitaire(string))
    
for k in total:
    print(k)