from math import factorial
n = int(input("n:"))
k = int(input("k:"))
print(int(factorial(n)/(factorial(k)*factorial((n-k)))))