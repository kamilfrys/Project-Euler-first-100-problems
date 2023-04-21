
def dtr(num):
    len_ = len(str(num))
    ans = ''
    if len_ >= 4:
        ans+=int(str(num)[:-3])*'M'
    if len_ >=3:
        if int(str(num)[-3:-2]) == 9:
            ans+='CM'
        elif int(str(num)[-3:-2]) >= 5:
            ans+='D'
            ans+=(int(str(num)[-3:-2])-5)*'C'
        elif int(str(num)[-3:-2]) == 4:
            ans+='CD'
        else: 
            ans+=int(str(num)[-3:-2])*'C'
    if len_>=2:
        if int(str(num)[-2:-1]) == 9:
            ans+='XC'
        elif int(str(num)[-2:-1]) >= 5:
            ans+='L'
            ans+=(int(str(num)[-2:-1])-5)*'X'
        elif int(str(num)[-2:-1]) == 4:
            ans+='XV'
        else: 
            ans+=int(str(num)[-2:-1])*'X'
    if len_ >=1:
        if int(str(num)[-1]) == 9:
            ans+='IX'
        elif int(str(num)[-1]) >= 5:
            ans+='V'
            ans+=(int(str(num)[-1])-5)*'I'
        elif int(str(num)[-1]) == 4:
            ans+='IV'
        else: 
            ans+=int(str(num)[-1])*'I'
    return ans

def rtd(num):
    dic = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
    ans = 0
    i = 0
    while i <= (len(num))-1:
        if i < len(num)-1:
            if num[i:i+2] in dic:
                ans+=dic[num[i:i+2]]
                i+=2
            else:
                ans+=dic[num[i]]
                i+=1
        else:
            ans+=dic[num[i]]
            i+=1
    return ans

ans = 0

filename = 'roman.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]

for i in lines:
    if i != dtr(rtd(i)):
        ans+=len(i)-len(dtr(rtd(i)))

print(ans)


