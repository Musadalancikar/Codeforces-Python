
def get_english_alphabet():
    return [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

alphabet = get_english_alphabet()

start_index = 0
n = input()
total = 0

for i in n:
    result = alphabet[:start_index+1][::-1] + alphabet[start_index:][::-1]
    result1 = result[::-1]
    for j in range(len(alphabet)):
        if result1[j] == i or result[j] == i:
            start_index = alphabet.index(i)
            break
        else:
            total += 1
    
print(total)
    
    
        




