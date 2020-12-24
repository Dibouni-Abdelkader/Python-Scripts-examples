from math import pi
def cube(n):
	return n**3
	
def volumeSphere (r):
	return 4*pi*cube(r)/3
	
r=input("entrez la valeur du rayon: ")
print ("la volume de cette sphere vaut ",volumeSphere(float(r))	)

print(cube(4))


		
