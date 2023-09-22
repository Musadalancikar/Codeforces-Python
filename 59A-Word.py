n = input()

lwr_nmbr = 0
uppr_nmbr = 0

for i in list(n):
    if i.islower() == True:
        lwr_nmbr += 1
    else:
        uppr_nmbr += 1
        
if lwr_nmbr == uppr_nmbr:
    print(n.lower())
    
elif lwr_nmbr > uppr_nmbr:
    print(n.lower())
    
else:
    print(n.upper())
    
    
    

    



