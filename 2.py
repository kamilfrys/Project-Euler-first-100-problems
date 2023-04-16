def fibonacci_num(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else: 
        a = 0
        b = 1
        for i in range(1,num):
            c = a + b
            a = b
            b = c
        return c

fibonacci_sum = 0
n = 1     

while True:
    if fibonacci_num(n) < 4000000:
        if fibonacci_num(n) % 2 ==0:
            fibonacci_sum = fibonacci_sum + fibonacci_num(n)
    else:
        break
    n = n + 1
    
print(fibonacci_sum)