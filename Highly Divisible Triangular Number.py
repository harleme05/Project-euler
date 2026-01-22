import math

def triangle_number(n):
    return n * (n + 1) // 2

def counting_divisors(n):
    count = 0
    r = math.isqrt(n)
    for i in range(1,r+1):
        if n % i == 0:
            count+=2
    if i*i==n:
            count-=1
    return(count)


def solve(limit=500):
    n = 1
    while True:
        t = triangle_number(n)
        d = counting_divisors(t)

        if d > limit:
            return t, n, d     

        n += 1

print(solve())
