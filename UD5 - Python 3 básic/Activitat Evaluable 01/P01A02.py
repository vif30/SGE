"""ACTIVITAT 2: En Python 3 els tipus simples es passen per valor
i els compostos per referència. Crea un exemple amb 3 funcions que: """

# - Reva 2 numeros i torne la suma:

def Suma(y, x):
    return(x + y)
Suma(6, 10)

""" - Reva una llista i modifique eixa mateixa llista (referència)
doblant els valors de tots els elements. No ha de retornar res."""
def doblaLista(lista):
    for idx in range(len(lista)):
        lista[idx] = lista[idx] * 2
lst = [1, 2, 3, 4, 5]
doblaLista(lst)

""" -	Reva una llista i torne una còpia de la llista mateixa
llista (referència) doblant els valors de tots els elements.
La llista original no hi ha de modificar-se."""
from copy import copy, deepcopy
def copiaDoblaLista(lista):
    listaCopia = deepcopy(lista)
    for idx in range(len(listaCopia)):
        listaCopia[idx] = listaCopia[idx] * 2
    return listaCopia    
lst2 = [5, 10, 15, 20, 25]
listaCopia = copiaDoblaLista(lst2)

