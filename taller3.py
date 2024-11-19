#EJERCICIO 1


import random

def tablero(alto, ancho, letra_rep, letra_unica):
    matriz = []

    for _ in range(alto): 
        fila = [] 
        for _ in range(ancho):  
            fila.append(letra_rep)
        matriz.append(fila)

    fila_azar = random.randint(0, alto - 1)
    columna_azar = random.randint(0, ancho - 1)

    matriz[fila_azar][columna_azar] = letra_unica

    return matriz


while True:
    print("Elija dentro de las siguientes opciones")
    print("1. Generar tablero por defecto, dimensiones 5x5 y letras 0 y 8")
    print("2. Elegir dimensiones y letras")
    print("3. Salir")
    
    opcion = input("Opción: ")

    if opcion == "1":
        alto = 5
        ancho = 5
        letra_rep = "0"
        letra_unica = "8"

        tablero1 = tablero(alto, ancho, letra_rep, letra_unica)       
        
        for fila in tablero1:
            print(fila)


    elif opcion == "2":
        dimensiones = input("ingresa las dimensiones del tablero: ")
        dimen_sep = dimensiones.split("x")
        alto = int(dimen_sep[0])
        ancho = int(dimen_sep[1])
        print(f"el alto del tablero será de {alto} y ancho de {ancho}")

        letra_rep = input("Ingrese la letra que desea se repita: ")
        letra_unica = input("Ingrese la letra que desea sea única: ")

        tablero2 = tablero(alto, ancho, letra_rep, letra_unica)       
        
        for fila in tablero2:
            print(fila)


    elif opcion == "3":
        print("Saliendo del programa ... ")
        break 

    else:
        print("Opción inválida. Por favor, ingrese un número válido.")


#EJERCICIO 2

pollito_pio = {
    "cancion" : """

En la radio, hay un pollito
En la radio, hay un pollito
El pollito pío, el pollito pío
El pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay una gallina
En la radio, hay una gallina
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gallo
En la radio, hay también un gallo
Y el gallo corococo, y la gallina coo
Y el pollito pío, el pollito pío
El pollito pío, el pollito pío

En la radio, hay un pavo
En la radio, hay un pavo
Y el pavo glugluglu, y el gallo corococo
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una paloma
En la radio, hay una paloma
Y la paloma ruuu, el pavo glugluglu
El gallo corococo, y la gallina coo
El pollito pío, el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un gato
En la radio, hay también un gato
Y el gato miao, la paloma ruuu
El pavo glugluglu, el gallo corococo
Y la gallina coo, y el pollito pío
El pollito pío, y el pollito pío

En la radio, hay también un perro
En la radio, hay también un perro
Y el perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una cabra
En la radio, hay una cabra
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un cordero
En la radio, hay un cordero
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay una vaca
En la radio, hay una vaca
Y la vaca moo, y el cordero bee
Y la cabra mee, el perro guau guau
El gato miao, y la paloma ruu
El pavo glugluglu, el gallo cocoroco
Y la gallina coo, y el pollito pío
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay también un toro
En la radio, hay también un toro
Y el toro muu, y la vaca moo
Y el cordero bee, y la cabra mee
El perro guau guau, el gato miao
La paloma ruu, el pavo glugluglu
El gallo cocoroco, y la gallina coo
Y el pollito pío, y el pollito pío
Y el pollito pío, y el pollito pío

En la radio, hay un tractor
En la radio, hay un tractor
Y el tractor brum, y el tractor brum
Y el tractor brum y el pollito oh-oh

"""
}

for linea in pollito_pio.values():
    lineas = linea.split('\n')

palabras = []
for linea in lineas:
    palabras.extend(linea.split(" "))

palabras_clean = [palabra for palabra in palabras if palabra]

print(palabras_clean)

cantidad_palabras = len(palabras_clean)
print(f"la cantidad de palabras en la canción es de: {cantidad_palabras}")

contador = 0
texto = pollito_pio["cancion"]

contador_pio = texto.count("pío")
contador_pollito = texto.count("pollito")

print(f"la palabra pío se encuentra un total de {contador_pio} veces y la palabra pollito un total de {contador_pollito} veces")



#EJERCICIO 3

baby_shark = {
    "cancion2" : """

Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark, doo doo doo doo doo doo
Baby shark!

Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark, doo doo doo doo doo doo
Mommy shark!

Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark, doo doo doo doo doo doo
Daddy shark!

Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark, doo doo doo doo doo doo
Grandma shark!

Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark, doo doo doo doo doo doo
Grandpa shark!

Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt, doo doo doo doo doo doo
Let’s go hunt!

Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away, doo doo doo doo doo doo
Run away!

Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last, doo doo doo doo doo doo
Safe at last!

It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end, doo doo doo doo doo doo
It’s the end!

"""
}

for linea in baby_shark.values():
    lineas = linea.split('\n')

palabras = []
for linea in lineas:
    palabras.extend(linea.split(" "))

palabras_clean = [palabra for palabra in palabras if palabra]

print(palabras_clean)

cantidad_palabras = len(palabras_clean)
print(f"la cantidad de palabras en la canción es de: {cantidad_palabras}")

contador = 0
texto = baby_shark["cancion2"]

contador_shark = texto.count("shark")
contador_doo = texto.count("doo")

print(f"la palabra shark se encuentra un total de {contador_shark} veces y la palabra doo un total de {contador_doo} veces")

#RETO

Menu = [
    ["ID004", "entrada", "ensalada"],
    ["ID008", "entrada", "sopa de tomate"],
    ["ID005", "entrada", "sopa de cebolla"],
    ["ID011", "bebida", "Jugo de Fresa"],
    ["ID012", "bebida", "Limonada Natural"],
    ["ID102", "plato fuerte", "pasta"],
    ["ID106", "plato fuerte", "lassagna"],
]

Menu_dicc = {
    "entrada":[ "ensalada", "sopa de tomate", "sopa de cebolla"],
    "bebida":["jugo de fresa", "Limonada Natural"],
    "plato fuerte": ["pasta", "lassagna"]
}


def imprimir_menu():
    print("Menú:")
    for item in Menu:
        tipo = item[1] 
        elemento = item[2] 
        print(f"{tipo} - {elemento}") 


def agregar_elemento(id, tipo, elemento):
    nuevo_elemento = [id, tipo, elemento]
    Menu.append(nuevo_elemento)
    
def filtrar_cat(categoria):
    found = False
    for item in Menu:
        tipo = item[1] 
        elemento = item[2]
        if categoria in tipo:
            print(elemento)
            found = True  
    if not found: 
        print("No se encontraron elementos")

def buscar(texto):
    found = False
    for item in Menu:
        elemento = item[2]
        if texto in elemento:
            print(elemento)
            found = True  
    if not found: 
        print("No se encontraron elementos")


def buscar_categoria(categoria):
    if categoria in Menu_dicc:
        return f"{categoria}: {Menu_dicc[categoria]}"
    else:
        return "No se encontraron elementos en esa categoría"  



while True:
    print("Opciones")
    print("1. Visualizar la información del menú")
    print("2. Agregar nuevos elementos al menú")
    print("3. Filtrar por una categoría")
    print("4. Buscar por un nombre")
    print("5. Visualizar nombres en categorías")
    print("6. Salir")

    opcion = input("Ingrese el número de opción que desea: ")


    if opcion == "1":
        menu_ordenado = imprimir_menu()
        print(menu_ordenado)


    elif opcion == "2":
        id = input("Ingrese el ID del nuevo elemento: ")
        tipo = input("Ingrese el tipo de elemento: ")
        elemento = input("Ingrese el elemento: ")
        menu_nuevo = agregar_elemento(id, tipo, elemento)    

        for item in Menu:
            print(item)

    elif opcion == "3":
        categoria = input("Ingrese el nombre de la categoría que desea ver: ")
        menu_filtrado = filtrar_cat(categoria)
        print(menu_filtrado)

    elif opcion == "4":
        texto = input("Ingrese texto de lo que desea encontrar: ")
        resultado = buscar(texto)
        print(resultado)


    elif opcion == "5":
        solicitud = input("Ingrese la categoría que desea filtrar: ")
        resultado = buscar_categoria(solicitud)
        print(resultado)


    elif opcion == "6":
        print("Saliendo del programa ... ")
        break 
    else:
        print("Opción inválida. Por favor, ingrese un número válido.")
