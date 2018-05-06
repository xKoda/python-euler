import math
def isPrime(n):
    if n==1:
        return False
    if n<4:
        return True
    if n%2==0:
        return False
    if n<0:
        return True
    if n%3==0:
        return False
    r = math.floor(math.sqrt(n))
    f = 5
    while f<=r:
        if n%f==0:
            return False
        if n%(f+2)==0:
            return False
        f+=6
    return True

outp=sum(x for x in range(1,2000000) if isPrime(x))

print(outp)
