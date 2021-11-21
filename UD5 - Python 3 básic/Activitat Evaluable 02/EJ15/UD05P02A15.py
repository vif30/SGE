import pyperclip
import sys

final = ""
consola = str(sys.argv[1])
f = open(consola, 'r')     #abrimos el archivo 
prohibidas = []

for x in f:     #Leemos el archivo, eliminando los saltos de linea y pasando a minusculas
    cortado = x.strip('\n')
    cortado = cortado.lower()
    prohibidas.append(cortado)      #Agregamos a la lista 

pyperclip.waitForNewPaste()     #Esperamos que el usuario haga un control+c nuevo
porta = pyperclip.paste().lower().split(" ")    #pasamos a minusculas y separamos las palabras por los espacios
#Recorremos las palabras del portapapeles 
for y in porta:     #Si es igual a alguna de las prohibidas la sustituimos por asteriscos
    if(y in prohibidas):
        cens = len(y) * "*"
        final += " " + cens     #y la añadimos al string final censurada
    else: 
        final += " " + y    #Sino, la añadimos sin censurar

#La devolvemos al portapapeles censurada en caso de contener alguna palabra prohibida
pyperclip.copy(final)