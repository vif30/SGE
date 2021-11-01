""" ACTIVITAT 7: Defineix la classe Car en Python 3. La classe tindrà
com atributs “matrícula” (numèrica) i “color”. Crea un mètode imprimir,
i a més dos mètodes que vulgues. En segon lloc, fes que el programa demane
un número “n” per teclat i es creen “n” instàncies de la classe, on cada
instància:
-	Cada “matricula” tindrà un número consecutiu des d’1 fins a “n”.
-	El “color” serà per a cada instància un color aleatori obtingut
        d’aquest llistat [“red”, “white”, “black”, “pink”, “blue”]
Finalment, el programa haurà d’imprimir els valors de les 10 primeres instàncies.
En cas que “n” siga menor que 10, només imprimirà “n” instàncies.
"""
import random
class Car(object):      #Clase car
    matricula = 0
    color = ""
    def __init__(self, matricula, color):   #Constructor 
        self.matricula = matricula
        self.color = color
   #Getters
    @property
    def get_matricula(self):
        return self.matricula
    @property
    def get_color(self):
        return self.color
    #Funció imprimir
    def imprimir(self):
        print("Matricula: ", self.matricula)
        print("Color: ", self.color)

    #Funció per a assignar un color aleatori 
def randomColor():
    numColor = random.randint(1, 5)
    Color = ""
    if(numColor == 1):
        Color = "red"
    elif(numColor == 2):
        Color = "white"
    elif(numColor == 3):
        Color = "black"
    elif(numColor == 4):
        Color = "pink"
    elif(numColor == 5):
        Color = "blue"
    return Color
    
#Demane'm a l'usuari la cuantitat de cotxes que vol crear
print("¿Cuantos coches quieres crear?")
n = int(input())
#Creem els cotxes
for i in range (n):
    matricula = i+1 
    color = randomColor()
    coch = Car(matricula, color)
    #Imprimim els primers 10 cotxes
    if(i < 10):
        coch.imprimir()


