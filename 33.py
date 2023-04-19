from itertools import product

def nwd_i(a, b):
    while b:
        a, b = b, a%b
    return a


list1 = [int(i) for i in range(12,100)]
list2 = [int (i) for i in range(13,100)]
prod = list(product(list1,list2))
res = []
ans1 = 1
ans2 = 1

for i in prod:
    if i[0]/i[1] >= 1:
        continue
    else:
        a = str(i[0])[0]
        b = str(i[0])[1]
        c = str(i[1])[0]
        d = str(i[1])[1]
        if a == c:
            if int(d) == 0:
                continue
            elif int(b)/int(d) == i[0]/i[1]:
                if i[0]%10 != 0:
                    res.append(i)
        elif a == d:
            if int(c) == 0:
                continue
            elif int(b)/int(c) == i[0]/i[1]:
                if i[0]%10 != 0:
                    res.append(i)
        elif b == c:
            if int(d) == 0:
                continue
            elif int(a)/int(d) == i[0]/i[1]:
                if i[0]%10 != 0:
                    res.append(i)
        elif b == d:
            if int(c) == 0:
                continue
            if int(a)/int(c) == i[0]/i[1]:
                if i[0]%10 != 0:
                    res.append(i)


for i in res:
    nwd = nwd_i(i[0],i[1])
    ans1 = ans1*(i[0]/nwd)
    ans2 = ans2*(i[1]/nwd)
    

print(int(ans2/nwd_i(ans1,ans2)))







