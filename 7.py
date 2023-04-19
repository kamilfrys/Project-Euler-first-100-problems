from primenum import is_prime

i = 1
j = 2
prime_list = []

while i <= 10001: 
    if is_prime(j):
        prime_list.append(j)
        i+=1
    j+=1

print(prime_list[10000])

