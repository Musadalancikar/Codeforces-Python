def word_on_paper(lst1):
    paper = []
    for j in range(8):
        for k in range(8):
            if lst1[j][k] != ".":
                paper.append(lst1[j][k])
    
    return paper
        
n = int(input())
result = []

for i in range(n):
    lst = []
    for h in range(8):
        lst.append(list(input()))

    result.append("".join(word_on_paper(lst)))

for l in result:
    print(l)    
    