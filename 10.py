from primenum import is_prime

list = [2]
a = 3

while True:
    if a >= 2000000:
        break
    else:
        if is_prime(a):
            list.append(a)
            
        a+=2
print(sum(list))
    
