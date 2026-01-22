odd_square_sum = 0
for n in range (1,772001):
    if n%2 != 0:
        odd_square_sum = odd_square_sum + n**2


print(odd_square_sum)

