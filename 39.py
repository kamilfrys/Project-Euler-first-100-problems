import statistics
from statistics import mode
 
def most_common(List):
    return(mode(List))

def pythagorean_triplet(k,n):
    ans = []
    ans.append(n**2-k**2)
    ans.append(2*n*k)
    ans.append(n**2+k**2)
    ans = sorted(ans)
    return ans

res = []

for i in range(2,22):
    for j in range(1,i):
        if sum(pythagorean_triplet(j,i)) <= 1000:
            res.append(pythagorean_triplet(j,i))
            iter = 2
            while True:
                test = [i*iter for i in pythagorean_triplet(j,i)]
                if sum(test) <= 1000:
                    res.append(test)
                    iter+=1
                else:
                    break

result = [] 
for i in res: 
    if i not in result: 
        result.append(i)

ans = []
for i in result:
    ans.append(sum(i))


print(most_common(ans))
   