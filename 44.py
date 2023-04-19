

pentagon = [int(i*(3*i-1)/2) for i in range(1,10001)]
pentagon_ = pentagon[:5000]
perm = []

#print(pentagon_)

for i in range(len(pentagon_)-1):
    for j in range(i+1,len(pentagon_)):
        temp = []
        temp.append(pentagon_[i])
        temp.append(pentagon_[j])
        perm.append(temp)

for i in perm:
    if i[0]+i[1] in pentagon and i[1]-i[0] in pentagon:
        print(i)
        print(i[1]-i[0])
        print('-----')