#ACTIVITAT 4: Explica amb exemples com funcionen els operadors “is”, “not”, “in” en Python 3.
# Operador "is", s'utilitza per a comprobar que dos variables referixen al mateix objecte
x = ["apple", "banana", "cherry"]
y = ["apple", "banana", "cherry"]
print(x is y)   #False
y = x
print(x is y)   #True

#Operador "not", s'utilitza per a comprobar si el valor d'una variable es true o false
z = 5
print(not z==5)    #Si la variable es True, retorna False
z = False
print(not z>10)    #Si es false, retorna True

#Operador "in", s'utilitza per a comprobar si un valor es troba en una seqüencia
fruits = ["apple", "banana", "cherry"] 
if "banana" in fruits: #Si "banana" se encuentra en fruits[]
  print("yes")         #Imprimimos "yes"
#Tambe s'utilitza per a iterar a traves d'una sentencia d'un for
for x in fruits:
  print(x) 
