import os
import cv2
from pyzbar.pyzbar import decode
#Metodo para leer las imagenes
def BarcodeReader(image):
	img = cv2.imread(image)	#Abrimos la imagen
	detectedBarcodes = decode(img)	#La decodificamos
	if not detectedBarcodes:	#Sino se detecta el codigo de barras lo imprimimos
		print("Barcode Not Detected or your barcode is blank/corrupted!")
	else:	
		for barcode in detectedBarcodes:	#Localizamos el codigo de barras en la imagen
			(x, y, w, h) = barcode.rect
			cv2.rectangle(img, (x-10, y-10),
						(x + w+10, y + h+10),
						(255, 0, 0), 2)
			if barcode.data!="":	#Si la informacion del codigo de barras contiene algo
				nombre = image.strip(".png")	#nombre del alumno
				id = str(barcode.data[10:11]).strip("b")	#id del alumno sacado del codigo de barras
				print(nombre + ":") #Impimimos la información
				print(id)
				

dir = "/home/vicente/SGE/UD05/Activitat Evaluable 02/EJ10/" #Directorio de las imagenes
fotos = []
with os.scandir(dir) as ficheros:	#Guardamos el nombre de las imagenes en la lista fotos
	for fichero in ficheros:
		fotos.append(fichero.name)

for foto in fotos:	#Recorremos todas las fotos de la lista sacando su información por pantalla
	BarcodeReader(foto)		#En este ejemplo las fotos se tienen que encontrar en el mismo directorio que el archivo .py