def find_winner(n, responses):
    max_quality = -1
    winner_index = -1

    for i in range(n):
        words, quality = responses[i]
        if words <= 10 and quality > max_quality:
            max_quality = quality
            winner_index = i + 1

    return winner_index

t = int(input())
for _ in range(t):
    n = int(input())
    responses = [tuple(map(int, input().split())) for _ in range(n)]

    winner = find_winner(n, responses)
    print(winner)
