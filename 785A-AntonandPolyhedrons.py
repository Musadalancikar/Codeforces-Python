n = int(input())
    
total = 0

for i in range(n):
    x = input()
    if x == "Icosahedron":
        total += 20
    
    elif x == "Cube":
        total += 6
        
    elif x == "Tetrahedron":
        total += 4

    elif x == "Octahedron":
        total += 8
        
    elif x == "Dodecahedron":
        total += 12    


print(total)