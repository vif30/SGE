import requests
#Pedimos al usuario la especie deseada
especie = input("Indique de que especie desea buscar:")

print("SOLICITANDO INFORMACIÓN DE INTERNET")
print("espere....")
#Debido a que hay que recorrer diversas paginas, la url la almacenamos incompleta
URL = 'https://rickandmortyapi.com/api/character?page='
#Recorremos un bucle del 1 al 42, puesto que hay 42 paginas en la API de R&M
for i in range(1, 43):
    URL2 = URL + str(i) #Concatenamos a la URL el numero de pagina
    data = requests.get(URL2)   #solicitamos a la API la informacion de la pagina
    data2 = data.json()         #convertimos a JSON
    for element in data2['results']:    #imprimimos los nombres de los personajes cuya especie sea igual
       if(element['species'] == especie):
            print(element['name'])
