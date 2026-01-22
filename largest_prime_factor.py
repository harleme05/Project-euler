
n = 600851475143
k = 2
while k*k <= n:
    if n%k == 0:
        n = n/k
    else:
        k = k+1 

print(n)


