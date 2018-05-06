from collections import Counter

def find_prime_factors(n):
    out = []
    while n%2==0:
        factor=2
        out.append(factor)
        n=n/2
    factor=3
    maxfactor=n**0.5
    while True:
        if not n>1 and not factor<=maxfactor:
            break
        while True:
            if n%factor==0:    
                out.append(factor)
                n=n/factor
                maxfactor=n**0.5
            else:
                break
        factor+=2
    return out

def find_number_of_factors(x):
    out = 1
    factors = Counter(find_prime_factors(x))
    factors = [factors[x] for x in factors]
    factors = [x+1 for x in factors]
    for x in factors:
        out=out*x
    return out

step = 1000
while True:
    num = int((step*(step+1))/2)
    num_factors = find_number_of_factors(num)
    if num_factors>500:
        print(num_factors)
        step-=1
    if num_factors<500:
        print(num_factors)
        step+=1







    
            
