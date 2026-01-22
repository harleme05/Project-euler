def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

def sum_primes():
    sum = 0
    for i in range(1,2000000):
        if is_prime(i) ==True:
            sum +=i
    return sum

print(sum_primes())
