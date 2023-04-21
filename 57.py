ans = []

for i in range(8,1001): 
    temp_ans = []  
    l = 1
    m = 2
    for j in range(i-1):
        l+=2*m
        l,m = m,l
    l+=m
    if len(str(l)) > len(str(m)):
        temp_ans.append(l)
        temp_ans.append(m)
        ans.append(temp_ans)


print(len(ans))
