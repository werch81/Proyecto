# funciones
def operaciones(a,b):
    suma = a + b
    resta = a - b
    mult = a * b
    div = a /  b
    return suma,resta,mult,div



num1,num2 = map (int,input().split())
resultado = operaciones(num1,num2)
print(resultado)
suma1,resta1,mult1,div1 = operaciones (num1,num2)
print(suma1,resta1,mult1,div1)