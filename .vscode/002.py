val = 0
fibs = [1,1]
i = 0
while True:
    if int(fibs[i]+fibs[i+1]) <= 4000000:
            fibs.append(fibs[i]+fibs[i+1])
            i+=1
    else:
        break
fibs.remove(1)

for i in fibs:
    if i%2==0:
        val+=i

print(val)
print(fibs)


