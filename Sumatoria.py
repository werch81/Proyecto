n = int (input ("Ingrese el numero para n: "))
m = int (input ("Ingrese el numero para m: "))
suma = 0
if n > m:
    print ("n debe ser menor que m")
else:
    for i in range(n,m+1):
        suma += i
    print (suma)