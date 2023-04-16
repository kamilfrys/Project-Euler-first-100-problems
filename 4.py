
def num_reverse(num):
    return int(str(num)[::-1])

a_num = 0
b_num = 0
largest_palindrome = 0

for a in range(100,1000):
    for b in range (100,1000):
        c = a * b
        if c == num_reverse(c):
            if c > largest_palindrome:
                largest_palindrome = c
                a_num = a
                b_num = b
        
    
print(largest_palindrome)
print(a_num)
print(b_num)