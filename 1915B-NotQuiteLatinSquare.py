def not_quite_latin_square(total_sq):
    for j in range(3):
        if "?" in total_sq[j]:
            if "A" not in total_sq[j]:
                return "A"
            elif "B" not in total_sq[j]:
                return "B"
            else:
                return "C"

t = int(input())

for i in range(t):
    sq1 = list(map(str, input()))
    sq2 = list(map(str, input()))
    sq3 = list(map(str, input()))
    total_sq = [sq1, sq2, sq3]
    print(not_quite_latin_square(total_sq))
    