

best = 0

for a in range(999,99,-1):
    for b in range(a,99, -1):
        p = a*b
        if p <= best:
            continue
        if str(p) == str(p)[::-1]:
            best = p

print(best)

            
    
