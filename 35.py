
a = input("Ingrese un Numero: ")

a= int(a)
b=1
for i in range(1,a+1):
	if (a==0):
		b=1
		break
	b = b*i 	

print (str(b))
