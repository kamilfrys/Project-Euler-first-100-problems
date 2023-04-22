from itertools import combinations

comb = list(combinations([0,1,2,3,4,5,6,7,8,9],6))
comb_ = list(combinations(comb,2))
comb__ = []
sn = ['01','04','09','16','25','36','49','64','81']
ans = 0

for i in comb_:
    comb__.append([list(i[0]),list(i[1])])

for i in comb__:
    if 6 in i[0] and 9 not in i[0]:
        i[0].append(9)
    elif 9 in i[0] and 6 not in i[0]:
        i[0].append(6)
    if 6 in i[1] and 9 not in i[1]:
        i[1].append(9)
    elif 9 in i[1] and 6 not in i[1]:
        i[1].append(6)

for i in comb__:
    flag = True
    for j in sn:
        if int(j[0]) in i[0] and int(j[1]) in i[1]:
            continue
        elif int(j[0]) in i[1] and int(j[1]) in i[0]:
            continue
        else:
            flag = False
            break
    if flag == True:
        ans+=1

print(ans)