""" ACTIVITAT 3: Partint d’un context on volem emmagatzemar un usuari
i la seua contrasenya. Fes un exemple que explica com es faria: """

import hashlib

idpass = []     #Creem la llista
for i in range (5):     #Bucle per a demanar a l'usuari 5 usuaris i contrasenyes
    print("Escribe tu usuario")
    usucif = hashlib.sha1(input().encode('utf-8'))  #Pasem a format hash
    print("Escribe tu contraseña")
    contrcif = hashlib.sha1(input().encode('utf-8'))    #Pasem a format hash
    idpass.append([usucif.hexdigest(), contrcif.hexdigest()])
    #Guardem l'usuari i contrasenya cifrats en hexadecimal en la llista
  
diccidpass = {}     #Creen el diccionari
for i in range (5):     #Bucle per a demanar a l'usuari 5 usuaris i contrasenyes
    print("Escribe tu usuario")
    usucif = hashlib.sha1(input().encode('utf-8'))  #Pasem a format hash
    print("Escribe tu contraseña")
    contrcif = hashlib.sha1(input().encode('utf-8'))    #Pasem a format hash
    diccidpass[usucif.hexdigest()] = contrcif.hexdigest()
    """Guardem l'usuari i contrasenya cifrats en hexadecimal en el diccionari
    l'usuari es l'index i la contrasenya es el valor"""
