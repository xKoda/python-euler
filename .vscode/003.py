num = 600851475143

def isPrime(x):
    if x==2:
        return True
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def find_nearest_pF(x):
    c = 2
    while True:
        if isPrime(c):
            if x%c==0:
                return int(x/c)
        c+=1

def find_largest_pF(x):
    while not isPrime(x):
        x = find_nearest_pF(x)     
    else:
        return x

print("Number: ", num)
print("Is prime?", isPrime(num))
print( "Largest prime factor:", find_largest_pF(num))
