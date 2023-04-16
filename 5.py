
def num_searcher():
    num = 20
    while True:
        if num%20==0:
            if num%19==0:
                if num%18==0:
                    if num%17==0:
                        if num%16==0:
                            if num%15==0:
                                if num%14==0:
                                    if num%13==0:
                                        if num%12==0:
                                            if num%11==0:
                                                return num
        num+=1

print(num_searcher())