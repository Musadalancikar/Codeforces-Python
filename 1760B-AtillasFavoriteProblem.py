def get_english_alphabet():
    return [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

alphabet = get_english_alphabet()

def favorite_problem(string):
    max_string = max(string)
    return alphabet.index(max_string) + 1

t = int(input())
total = []

for i in range(t):
    n = int(input())
    string = input()
    total.append(favorite_problem(string))
    
for j in total:
    print(j)