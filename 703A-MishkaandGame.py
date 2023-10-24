
t = int(input())
m_total = 0
c_total = 0

for i in range(t):
    m, c = list(map(int, input().split()))
    if m > c:
        m_total += 1
    elif c > m:
        c_total += 1
    else:
        m_total = m_total
        c_total = c_total

if m_total > c_total:
    print("Mishka")
    
elif c_total > m_total:
    print("Chris")
    
else:
    print("Friendship is magic!^^")