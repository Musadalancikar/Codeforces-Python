def square_string(string):
    if len(string) % 2 == 0:
        if string[:int(len(string)/2)] == string[int(len(string)/2):]:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"

t = int(input())
total_result = []

for i in range(t):
    string = input()
    total_result.append(square_string(string))
    
for j in total_result:
    print(j)