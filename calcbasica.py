def operaciones(a,b,oper):
    if (oper == '1'):
        res = a + b
    elif (oper == '2'):
        res = a - b
    elif (oper == '3'):
        res = a * b
    elif (oper == '4'):  
        res = a /  b
    else:
        res = "operacion incorrecta"
    return res


oper1 = input ('Ingrese el numero de operacion a realizar : (1)suma, (2)resta , (3)multiplicacion y (4)division :  ')
num1,num2 = map (float,input().split())
print (operaciones(num1,num2,oper1))