

ans = 0

for i in range(1,100):
    for j in range(1,100):
        temp_pow = str(i**j)
        temp_sum = 0
        for k in temp_pow:
            temp_sum+=int(k)
        if temp_sum > ans:
            ans = temp_sum

print(ans)
