

res = []
for i in range(1,200000):
    for j in str(i):
        res.append(int(j))

print(res[0]*res[9]*res[99]*res[999]*res[9999]*res[99999]*res[999999])