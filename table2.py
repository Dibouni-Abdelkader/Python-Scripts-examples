def table(base,debut,fin):
	print("the multi par",base,'is:')
	n=debut
	while n<=fin:
		print (n,"x",base,"=",n*base)
		n=n+1
		
t, d, f = 11, 5, 10
while t<21:
	table(t,d,f)
	t, d, f = t +1, d +3, f +5


