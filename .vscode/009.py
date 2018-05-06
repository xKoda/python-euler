a = 1
b = 1
c = 1
while True:
	try:
		if (1000*(a - 500))%(a - 1000) ==0 and (a**2 - 1000*a + 500000)%(1000 - a)==0:
			b=(1000*(a - 500))/(a - 1000)
			c=(a**2 - 1000*a + 500000)/(1000 - a)
			break
		else:
			a+=1
	except ZeroDivisionError:
		a+=1

print(a,b,c)
print(a*b*c)

