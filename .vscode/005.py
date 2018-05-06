num = 20

def isDiv19(x):
    isDiv = True
    for i in range(19,1,-1):
        if x%i != 0:
            isDiv = False
    return isDiv


while True:
    if isDiv19(num):
        print("Found!", num)
        break
    else:
        if num%1000000==0:
            print("Now at:", num)
        num+=20


