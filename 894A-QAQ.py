def qaq(n):
    result = 0
    for i in range(len(n)):
        if n[i] == "Q":
            for j in range(i, len(n)):
                if n[j] == "A":
                    for z in range(j, len(n)):
                        if n[z] == "Q":
                            result += 1
    return result

n = input()

print(qaq(n))