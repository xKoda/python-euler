sumsquare = 0
squaresum = 0

for i in range(101):
    sumsquare+=i*i

for i in range(101):
    squaresum+=i

squaresum = squaresum * squaresum
difference = squaresum - sumsquare
print(difference)

