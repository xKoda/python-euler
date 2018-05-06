def chain(n):
    chain=[n]
    while n!=1:
        if n%2==0:
            chain.append(int(n/2))
        else:
            chain.append(int((3*n)+1))
        n=chain[-1]
    return len(chain)

n=2
count=[0,0]
while n<1000000:
    if count[-1]<chain(n):
        del count[-1]
        del count[-1]
        count.append(n)
        count.append(chain(n))
    print(n)
    print(count)
    n+=1
print(count)
