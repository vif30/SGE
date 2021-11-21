texto = input("Escribe una cadena de texto: ")

def numeroPatrones(text):
    text = text.lower()     #Pasamos a minusculas para que no haya diferencias
    cont00 = 0          #Contador de 00
    x, y = " ", " "     #Inicializamos x e y vacíos
    for i in text:      #Bucle que recorre cada uno de los char del string
        if(i == "0"):   #Si i es igual a 0
            x = i       #x = 0
            if(x == y):     #Si x=y es decir 0 = 0
                cont00 += 1 #+1 al contador
                x = ""      #Reiniciamos x
            else:       #Sino, y=0 y x=""
                y = x
                x = ""
        else:           #Si i!=0 reiniciamos x e y
            x, y = "", ""
    a, b, h, cero, uno = False, False, False, False, False  #inicializamos los valores como False
    contABC = 0     #Contadores
    contHO = 0
    cont101 = 0
    for j in text:      #Leemos la cadena de texto char a char
        if(j == "a"):   #Si es = a, a = True. Reseteamos el resto de valores
            a = True
            b, h, cero, uno = False, False, False, False
        elif(j == "b" and a == True):   #Si es = b y a=True, b = True 
            b = True
        elif(j == "c" and a == True and b == True):     #Si es = c y a y b son true +1 al contABC y reseteamos a y b
            contABC += 1
            a, b = False, False
        elif(j == "h"):     #Si es = h, h = True y reseteamos el resto de valores
            h = True
            a, b, cero, uno = False, False, False, False
        elif(j == "o" and h == True):   #Si es = O y h=True +1 al contHO y reseteamos h
            contHO += 1
            h = False
        elif(j == "1" and cero == False):   #Si es = 1 y 0=False, uno=True y reseteamos el resto 
            uno = True
            a, b, h = False, False, False
        elif(j == "0" and uno == True and cero == True):    #Si es =0 y uno y cero ya son True, reseteamos uno
            uno = False
        elif(j == "0" and uno == True):     #Si es=0 y uno=True, cero=True
            cero = True
        elif(j == "1" and uno == True and cero == True):    #Si es = 1 y uno y cero = True +1 a cont101 y reseteamos cero
            cont101 += 1
            cero = False
        #Si no es ninguna de las anteriores, reseteamos todas la variables
        else:
            a, b, h, cero, uno = False, False, False, False, False
    #Imprimimos todos los contadores
    print("Patrón 00: " + str(cont00))
    print("Patrón ABC: " + str(contABC))
    print("Patrón HO: " + str(contHO))
    print("Patrón 101: " + str(cont101))

numeroPatrones(texto)