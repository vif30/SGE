"""ACTIVITAT 6: Crea un llistat en el qual cada element d’eixa llista siga una
llista amb dos valors: mida i pes. Utilitzant les “key functions”, fer que
aquesta llista s’ordene per major altura i en cas d’igualtat, per menor pes. """
import operator
from copy import copy, deepcopy
a = []      #Creem la llista 'a'
a.append([1.80, 55])    #Afegim les dades
a.append([1.80, 100])
a.append([1.80, 75])
a.append([1.60, 105])    
a.append([1.80, 65])
a.append([1.90, 120])
a.append([2.0, 155])
#Ordenem primer per pes de menor a major
a.sort(key=operator.itemgetter(1)) #La key es l'item[1] de la llista
#Copiem la llista per a que es guarde l'ordre
b = deepcopy(a)
#Ordenem per altura de major a menor
b.sort(key=operator.itemgetter(0), reverse=True)    #La key es l'item [0] 
"""Tenim la llista ordenada per altura de major a menor i en cas
d'empat per pes de menor a major"""
print(a)
print(b)
