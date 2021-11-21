archivo = open('Sudoku.in', 'r')   #Abrimos el archivo Sudoku.in
sudoku = []
for linea in archivo:       #Leemos linea a linea el archivo
    lista = []
    cortado = linea.strip('\n')     #Eliminamos el salto de linea del final
    separado = cortado.split(" ")   #Separamos por espacios
    for x in separado:      #Recorremos la linea ya separada
        lista.append(x)     #Añadimos cada numero a la lista
    sudoku.append(lista)    #Añadimos la lista a la lista2 para conseguir un array bidimensional
    

def esSudokuCorrecto(miArrayBi):
    valido = True   #inicializamos valico con True
    for i in range(9):  #Recorremos del 0 al 8
        lin = []        #inicializamos el array de la linea
        for j in range(9):  #Recorremos de nuevo del 0 al 8
            if(miArrayBi[i][j] in lin): #Si la posicion [i][j] esta en lin[]
                valido = False      #El sudoku ya no es válido
            else:
                lin.append(miArrayBi[i][j]) #Sino, añadimos a lin
        #Al terminar la primera linea, reiniciamos lin y volvemos a empezar con
        #la linea siguiente
    
    for k in range(9):  #Igual que antes, recorremos el sudoku, pero en este caso,
        col = []    #sus columnas, y de la misma manera, si se repite algun numero
        for y in range(9):
            if(miArrayBi[y][k] in col):
                valido = False  #El array no es válido
            else:
                col.append(miArrayBi[y][k])
    return valido   #Si no se ha repetido ningún numero, devuelve true, en caso 
    #contrario, devuelve false
            

print(esSudokuCorrecto(sudoku))