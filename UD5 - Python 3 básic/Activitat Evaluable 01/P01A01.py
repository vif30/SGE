#ACTIVITAT 1: Prepara amb un exemple on expliques com fer en Python3:

# - Clonar una llista. ¿Quina és la diferència en Python entre “shallow copy” i “deep copy”?

#Métode copy()
fruits_spring=['carrots', 'kiwi', 'grapes', 'cherry']
fruits_summer = fruits_spring.copy()

""" Métode shallowcopy construeix un nou objecte de col·lecció que s’ompli amb 
referencies als objectes secundaris del original.Si es canvia algun element 
en la copia, es reflecteix en el objecte original."""
import copy
fruits_spring = ['carrots', 'kiwi', 'grapes', 'cherry']
fruits_summer = copy.copy(fruits_spring)

""" Métode deepcopy construeix un nou objecte que s’ompli amb 
copies dels objectes secundaris del original. Si es canvia algun 
element en la copia, no es reflecteix en el objecte original. """
import copy
fruits_spring = ['carrots', 'kiwi', 'grapes', 'cherry']
fruits_summer = copy.deepcopy(fruits_spring)

# - Afegir un element a una llista
fruits_summer.append("watermelon")

# - Llevar un element a una llista
""".remove(): indiquem en el parèntesis el element que desitgem eliminar 
de la llista, y aquest eliminarà el primer element que trobe."""
fruits_spring.remove("kiwi")

#.pop(): indiquem en el parèntesis l’index del element que volem eliminar.
fruits_summer.pop(2)

#del: funciona igual que .pop, indiquem al parèntesis l’index del element que volem eliminar.
del fruits_spring[3]

# - Crear una nova llista amb els 4 últims elements d’una llista.
li1 = [1,2,3,4,5,6,7,8,9]
li2 = [li1[len(li1) - 4], li1[len(li1) - 3], li1[len(li1) - 2], li1[len(li1) - 1], 88, 99, 123]

# - Convertir les paraules d’una cadena (separades per espai) a una llista.
string = "Esto es un ejemplo de .split()"
lista = string.split(' ')

# - Comentaris amb una línia.
#Açò es un comentari de una línia.

# - Comentaris multi línia.
""" Açò es un 
Comentari
multi línia."""
