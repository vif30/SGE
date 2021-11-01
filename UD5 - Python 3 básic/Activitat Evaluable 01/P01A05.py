#ACTIVITAT 5:
""" - Posa un exemple de com passar diversos
paràmetres des de consola a un programa Python 3."""
"""Per a pasar diversos parametres per consola simplement em de separarlo per
espais quan cridem al programa, el següent exemple conta el parametres
que pasem per consola i els imprimix"""
import sys
print ("Número de parámetros: ", len(sys.argv))
print ("Lista de argumentos: ", sys.argv)

""" Posa un exemple de com fer “sobrecàrrega de funcions”
(funcions que poden rebre diversos números de paràmetres),
incloent el cas de què el nombre de paràmetres no siga definit. """
""" El següent exemple crea una funció que segons el nombre de parametres
que reba, fara una cosa o otra, es aquest cas, imprimir. """
class Home:
    def Knock(self, person_one=None, person_two=None):
        if person_one is not None and person_two is None:
            print("Hi, " + person_one)
        elif person_one is not None and person_two is not None:
            print("Hi, " + person_one + " and " + person_two)
        else: 
            print("Who's there? ")

DefObj = Home()

DefObj.Knock()
DefObj.Knock('Rick','Morty')
DefObj.Knock('Sam')
