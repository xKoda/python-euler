def isPrime(x):
    if x==2:
        return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def compute():
    c = 0
    p = 2
    while c != 10001:
        if isPrime(p):
            c+=1
            print("Now at ", c, p)
            if c == 10001:
                print("Found!", c, p)
            p+=1
        else:
            p+=1

compute()





