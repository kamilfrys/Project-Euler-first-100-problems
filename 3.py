
def prime_factors_searcher(num):
    prime_factors = []
    n = 2
    while num != 1:
        while num % n ==0:
            num = num // n
            prime_factors.append(n)
        n = n + 1

    return prime_factors

    
print((prime_factors_searcher(600851475143)))