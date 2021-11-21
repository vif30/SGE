"""a) Funcion lambda que recibe un número y devuelve true si su cuadrado 
es mayor o igual a 10, y false si es menor de 10"""
lambda_func = lambda x: True if x**2 >= 10 else False
print(lambda_func(3)) # Retorna False
print(lambda_func(4)) # Retorna True

"""b) Funcion Python que realiza la misma funcion que la del apartado a)
recibe un numero y si su cuadrado es mayor o igual que 10 devuelve true,
si es menor, false. Se puede comprobrar que con la funcion lambda ahorramos 
bastantes lineas de código, por lo que es una buena idea utilizarlas"""
def cuadrado(num):
    if(num ** 2 >= 10):
        return True
    else: 
        return False

print(cuadrado(5))  #Retorna True
print(cuadrado(3))  #Retorna False

"""c) """
def separar(cadena):
    return cadena.split(' ')
     
print("Escribe una cadena de de números separados por espacios")
nums = "1 2 3 4 5"
cadena = separar(nums)
if(cadena.isdigit()):
    print(cadena)
#print(cadena)
#lista = list(map(separar, nums))

#raise ValueError("Debe escribir unicamente digitos")
#print(lista)