

y, w = list(map(int, input().split()))

max_score = max(y,w)

total = 6

probability_up = total - max_score + 1

if probability_up == 0:
    print("0/1")
    
elif probability_up == total:
    print("1/1")
    
else:
    if probability_up % 2 == 0:
        print(f"{int(probability_up/2)}/{int(total/2)}")
    elif total % probability_up == 0 and probability_up > 1:
        print(f"{int(1)}/{int(total/probability_up)}")
    else:
        print(f"{probability_up}/{total}")

