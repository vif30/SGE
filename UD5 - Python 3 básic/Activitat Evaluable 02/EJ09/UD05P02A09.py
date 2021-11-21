import csv
import sys
from barcode import EAN13
from barcode.writer import ImageWriter

consola = str(sys.argv[1])

def ean_checksum(code: str) -> int:     #Metodo para calcular el codigo de control del EAN13, al que le pasamos nuestro codigo EAN13
    digits = [int(i) for i in reversed(code)]
    return (10 - (3 * sum(digits[0::2]) + (sum(digits[1::2])))) % 10

with open(consola, newline='') as File:  #Abrimos el archivo consola
    reader = csv.reader(File)   #leemos el .csv
    for row in reader:      #repetimos por cada fila del archivo    
        id = row[1]         #sacamos el id del alumno
        number = '8401234000' + id  #creamos el numero EAN13, 840 por españam 1234 como numero de empresa, 2 ceros mas el id del alumno
        number += str(ean_checksum(number)) #añadimos al final el numero de control calculado por el metodo
        my_code = EAN13(number, writer=ImageWriter())   #Creamos la imagen con el codigo de barras pasando como argumento el nuestro numero EAN13
        my_code.save(row[0])    #guardamos la imagen con el nombre del alumno
