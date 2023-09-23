

def foncution(n):
    if n % 2 == 0:    
        x = int(n / 2)
        return (x * (x+1)) - (x ** 2)
    else:
        x = int((n-1)/2)
        y = int((n+1)/2)
        return (x * (x+1)) - (y ** 2)
          
n = int(input())

print(foncution(n))