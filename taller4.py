#JUEGO 1
"""
0 empate
1 gana jugador 1
2 gana jugador 2

Pierda vs piedra= 0
Piedra vs papel = 2
Piedra vs tijeras = 1 

Papel vs piedra = 1
Papel vs papel = 0 
Papel vs tijeras = 2

Tijeras vs piedra = 2
Tijeras vs papel = 1
Tijeras vs tijeras = 0 
"""

import random
matriz_1= [
    [0, 2, 1],
    [1, 0, 2],
    [2, 1, 0]
]

victorias_maq = 0
victorias_jug = 0
empates = 0

while True:
    print("Elija la opción deseada:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    maquina = random.randint(1,3)
    text_jugador = input("Ingrese la opción que desea: ")
    jugador = text_jugador.lower()

    if jugador == "salir":
        print("Gracias por jugar. Hasta pronto")
        break
    
    if maquina == 1:
        decision_maq = "piedra"
    elif maquina == 2:
        decision_maq = "papel"
    elif maquina == 3:
        decision_maq = "tijera"


    if jugador == "piedra":
        decision_jug = 1
    elif jugador == "papel":
        decision_jug = 2
    elif jugador == "tijera":
        decision_jug = 3
    else: 
        print("Decisión errónea, por favor vuelva a empezar")
        continue

    resultado = matriz_1[maquina-1][decision_jug-1]

    if resultado == 0:
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ha habido un empate")
    elif resultado == 1:
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ganó la máquina")
    else: 
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ganó usted")
        

    if resultado == 1:
        victorias_maq += 1
    elif resultado == 0:
        empates += 1
    else: 
        victorias_jug += 1


    
    print(
        f"""
        La tabla va de la siguiente manera:
        Máquina = {victorias_maq}
        Jugador = {victorias_jug}
        Empates = {empates}
        """
    )



#JUEGO 2
"""
0 empate
1 gana jugador 1
2 gana jugador 2

Pierda vs piedra= 0
Piedra vs agua = 2
Piedra vs aire = 2
Pierda vs papel= 2
Piedra vs esponja = 1
Piedra vs tijera = 1
Piedra vs fuego = 1

agua vs piedra= 1
agua vs agua = 0
agua vs aire = 2
agua vs papel= 2
agua vs esponja = 2
agua vs tijera = 1
agua vs fuego = 1

aire vs piedra= 1
aire vs agua = 1
aire vs aire = 0
aire vs papel= 2
aire vs esponja = 2
aire vs tijera = 2
aire vs fuego = 1

papel vs piedra= 1
papel vs agua = 1
papel vs aire = 1
papel vs papel= 0
papel vs esponja = 2
papel vs tijera = 2
papel vs fuego = 2

esponja vs piedra= 2
esponja vs agua = 1
esponja vs aire = 1
esponja vs papel= 1
esponja vs esponja = 0
esponja vs tijera = 2
esponja vs fuego = 2

tijera vs piedra= 2
tijera vs agua = 2
tijera vs aire = 1
tijera vs papel= 1
tijera vs esponja = 1
tijera vs tijera = 0
tijera vs fuego = 2

fuego vs piedra= 2
fuego vs agua = 2
fuego vs aire = 2
fuego vs papel= 1
fuego vs esponja = 1
fuego vs tijera = 1
fuego vs fuego = 0

"""

import random
matriz_1= [
    [0, 2, 2, 2, 1, 1, 1],
    [1, 0, 2, 2, 2, 1, 1],
    [1, 1, 0, 2, 2, 2, 1],
    [1, 1, 1, 0, 2, 2, 2],
    [2, 1, 1, 1, 0, 2, 2],
    [2, 2, 1, 1, 1, 0, 2],
    [2, 2, 2, 1, 1, 1, 0]
]

victorias_maq = 0
victorias_jug = 0
empates = 0

while True:
    print("Elija la opción deseada:")
    print("1. Piedra")
    print("2. Agua")
    print("3. Aire")
    print("4. Papel")
    print("5. Esponja")
    print("6. Tijera")
    print("7. Fuego")
    print("8. Salir")

    maquina = random.randint(1,7)
    text_jugador = input("Ingrese la opción que desea: ")
    jugador = text_jugador.lower()

    if jugador == "salir":
        print("Gracias por jugar. Hasta pronto")
        break
    
    if maquina == 1:
        decision_maq = "piedra"
    elif maquina == 2:
        decision_maq = "agua"
    elif maquina == 3:
        decision_maq = "aire"
    elif maquina == 4:
        decision_maq = "papel"
    elif maquina == 5:
        decision_maq = "esponja"
    elif maquina == 6:
        decision_maq = "tijera"
    elif maquina == 7:
        decision_maq = "fuego"


    if jugador == "piedra":
        decision_jug = 1
    elif jugador == "agua":
        decision_jug = 2
    elif jugador == "aire":
        decision_jug = 3
    elif jugador == "papel":
        decision_jug = 4
    elif jugador == "esponja":
        decision_jug = 5
    elif jugador == "tijera":
        decision_jug = 6
    elif jugador == "fuego":
        decision_jug = 7
    else: 
        print("Decisión errónea, por favor vuelva a empezar")
        continue

    resultado = matriz_1[maquina-1][decision_jug-1]

    if resultado == 0:
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ha habido un empate")
    elif resultado == 1:
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ganó la máquina")
    else: 
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ganó usted")
        
    if resultado == 1:
        victorias_maq += 1
    elif resultado == 0:
        empates += 1
    else: 
        victorias_jug += 1


    print(
        f"""
        La tabla va de la siguiente manera:
        Máquina = {victorias_maq}
        Jugador = {victorias_jug}
        Empates = {empates}
        """
    )



#JUEGO 3
"""
0 empate
1 gana jugador 1
2 gana jugador 2


piedra vs piedra= 0
piedra vs arma = 2
piedra vs relámpago = 2
piedra vs demonio= 2
piedra vs dragon = 2
piedra vs agua = 2
piedra vs aire = 2
piedra vs papel= 2
piedra vs esponja = 1
piedra vs lobo = 1
piedra vs árbol = 1
piedra vs humano = 1
piedra vs serpiente = 1
piedra vs tijera = 1
piedra vs fuego = 1

arma vs piedra= 1
arma vs arma = 0
arma vs relámpago = 2
arma vs demonio= 2
arma vs dragon = 2
arma vs agua = 2
arma vs aire = 2
arma vs papel= 2
arma vs esponja = 2
arma vs lobo = 1
arma vs árbol = 1
arma vs humano = 1
arma vs serpiente = 1
arma vs tijera = 1
arma vs fuego = 1

relámpago vs piedra= 1
relámpago vs arma = 1
relámpago vs relámpago = 0 
relámpago vs demonio= 2
relámpago vs dragon = 2
relámpago vs agua = 2
relámpago vs aire = 2
relámpago vs papel= 2
relámpago vs esponja = 2
relámpago vs lobo = 2
relámpago vs árbol = 1
relámpago vs humano = 1
relámpago vs serpiente = 1
relámpago vs tijera = 1
relámpago vs fuego = 1

demonio vs piedra = 1
demonio vs arma = 1
demonio vs relámpago = 1
demonio vs demonio = 0
demonio vs dragon = 2
demonio vs agua = 2
demonio vs aire = 2
demonio vs papel= 2
demonio vs esponja = 2
demonio vs lobo = 2
demonio vs árbol = 2
demonio vs humano = 1
demonio vs serpiente = 1
demonio vs tijera = 1
demonio vs fuego = 1

dragon vs piedra = 1
dragon vs arma = 1
dragon vs relámpago = 1
dragon vs demonio = 1
dragon vs dragon = 0
dragon vs agua = 2
dragon vs aire = 2
dragon vs papel= 2
dragon vs esponja = 2
dragon vs lobo = 2
dragon vs árbol = 2
dragon vs humano = 2
dragon vs serpiente = 1
dragon vs tijera = 1
dragon vs fuego = 1

agua vs piedra= 1
agua vs arma = 1
agua vs relámpago = 1
agua vs demonio= 1
agua vs dragon = 1
agua vs agua = 0
agua vs aire = 2
agua vs papel= 2
agua vs esponja = 2
agua vs lobo = 2
agua vs árbol = 2
agua vs humano = 2
agua vs serpiente = 2
agua vs tijera = 1
agua vs fuego = 1

aire vs piedra= 1
aire vs arma = 1
aire vs relámpago = 1
aire vs demonio= 1
aire vs dragon = 1
aire vs agua = 1
aire vs aire = 0
aire vs papel= 2
aire vs esponja = 2
aire vs lobo = 2
aire vs árbol = 2
aire vs humano = 2
aire vs serpiente = 2
aire vs tijera = 2
aire vs fuego = 1

papel vs piedra= 1
papel vs arma = 1
papel vs relámpago = 1
papel vs demonio= 1
papel vs dragon = 1
papel vs agua = 1
papel vs aire = 1
papel vs papel= 0
papel vs esponja = 2
papel vs lobo = 2
papel vs árbol = 2
papel vs humano = 2
papel vs serpiente = 2
papel vs tijera = 2
papel vs fuego = 2

esponja vs piedra = 2
esponja vs arma = 1
esponja vs relámpago = 1
esponja vs demonio = 1
esponja vs dragon = 1
esponja vs agua = 1
esponja vs aire = 1
esponja vs papel= 1
esponja vs esponja = 0
esponja vs lobo = 2
esponja vs árbol = 2
esponja vs humano = 2
esponja vs serpiente = 2
esponja vs tijera = 2
esponja vs fuego = 2

lobo vs piedra= 2
lobo vs arma = 2
lobo vs relámpago = 1
lobo vs demonio= 1
lobo vs dragon = 1
lobo vs agua = 1
lobo vs aire = 1
lobo vs papel= 1
lobo vs esponja = 1
lobo vs lobo = 0
lobo vs árbol = 2
lobo vs humano = 2
lobo vs serpiente = 2
lobo vs tijera = 2
lobo vs fuego = 2

árbol vs piedra = 2
árbol vs arma = 2
árbol vs relámpago = 2
árbol vs demonio = 1
árbol vs dragon = 1 
árbol vs agua = 1
árbol vs aire = 1
árbol vs papel= 1
árbol vs esponja = 1
árbol vs lobo = 1
árbol vs árbol = 0
árbol vs humano = 2
árbol vs serpiente = 2
árbol vs tijera = 2
árbol vs fuego = 2

humano vs piedra= 2
humano vs arma = 2
humano vs relámpago = 2
humano vs demonio = 2
humano vs dragon = 1
humano vs agua = 1
humano vs aire = 1
humano vs papel= 1
humano vs esponja = 1
humano vs lobo = 1
humano vs árbol = 1
humano vs humano = 0
humano vs serpiente = 2
humano vs tijera = 2
humano vs fuego = 2

serpiente vs piedra = 2
serpiente vs arma = 2
serpiente vs relámpago = 2
serpiente vs demonio = 2
serpiente vs dragon = 2
serpiente vs agua = 1
serpiente vs aire = 1
serpiente vs papel= 1
serpiente vs esponja = 1
serpiente vs lobo = 1
serpiente vs árbol = 1
serpiente vs humano = 1
serpiente vs serpiente = 0
serpiente vs tijera = 2
serpiente vs fuego = 2

tijera vs piedra = 2
tijera vs arma = 2
tijera vs relámpago = 2
tijera vs demonio = 2
tijera vs dragon = 2
tijera vs agua = 2
tijera vs aire = 1
tijera vs papel = 1
tijera vs esponja = 1
tijera vs lobo = 1
tijera vs árbol = 1
tijera vs humano = 1
tijera vs serpiente = 1
tijera vs tijera = 0
tijera vs fuego = 2

fuego vs piedra = 2
fuego vs arma = 2
fuego vs relámpago = 2 
fuego vs demonio = 2
fuego vs dragon = 2
fuego vs agua = 2
fuego vs aire = 2
fuego vs papel= 1
fuego vs esponja = 1
fuego vs lobo = 1
fuego vs árbol = 1
fuego vs humano = 1
fuego vs serpiente = 1
fuego vs tijera = 1
fuego vs fuego = 0
"""

import random
matriz_1= [
    [0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
    [1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 1, 1],
    [1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2, 2],
    [2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2, 2],
    [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2, 2],
    [2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2, 2],
    [2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2, 2],
    [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0]
]

victorias_maq = 0
victorias_jug = 0
empates = 0

while True:
    print("Elija la opción deseada:")
    print("1. Piedra")
    print("2. Arma")
    print("3. Relámpago")
    print("4. Demonio")
    print("5. Dragon")
    print("6. Agua")
    print("7. Aire")
    print("8. Papel")
    print("9. Esponja")
    print("10. Lobo")
    print("11. Árbol")
    print("12. Humano")
    print("13. Serpiente")
    print("14. Tijera")
    print("15 Fuego")
    print("16. Salir")

    maquina = random.randint(1,15)
    text_jugador = input("Ingrese la opción que desea: ")
    jugador = text_jugador.lower()

    if jugador == "salir":
        print("Gracias por jugar. Hasta pronto")
        break
    
    if maquina == 1:
        decision_maq = "piedra"
    elif maquina == 2:
        decision_maq = "arma"
    elif maquina == 3:
        decision_maq = "relámpago"
    elif maquina == 4:
        decision_maq = "demonio"
    elif maquina == 5:
        decision_maq = "dragon"
    elif maquina == 6:
        decision_maq = "agua"
    elif maquina == 7:
        decision_maq = "aire"
    elif maquina == 8:
        decision_maq = "papel"
    elif maquina == 9:
        decision_maq = "esponja"
    elif maquina == 10:
        decision_maq = "lobo"
    elif maquina == 11:
        decision_maq = "árbol"
    elif maquina == 12:
        decision_maq = "humano"
    elif maquina == 13:
        decision_maq = "serpiente"
    elif maquina == 14:
        decision_maq = "tijera"
    elif maquina == 15:
        decision_maq = "fuego"


    if jugador == "piedra":
        decision_jug = 1
    elif jugador == "arma":
        decision_jug = 2
    elif jugador == "relámpago":
        decision_jug = 3
    elif jugador == "demonio":
        decision_jug = 4
    elif jugador == "dragon":
        decision_jug = 5
    elif jugador == "agua":
        decision_jug = 6
    elif jugador == "aire":
        decision_jug = 7
    elif jugador == "papel":
        decision_jug = 8
    elif jugador == "esponja":
        decision_jug = 9
    elif jugador == "lobo":
        decision_jug = 10
    elif jugador == "arbol":
        decision_jug = 11
    elif jugador == "humano":
        decision_jug = 12
    elif jugador == "serpiente":
        decision_jug = 13
    elif jugador == "tijera":
        decision_jug = 14
    elif jugador == "fuego":
        decision_jug = 15
    else: 
        print("Decisión errónea, por favor vuelva a empezar")
        continue

    resultado = matriz_1[maquina-1][decision_jug-1]

    if resultado == 0:
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ha habido un empate")
    elif resultado == 1:
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ganó la máquina")
    else: 
        print(f"La máquina ha escogido {decision_maq} y usted ha escogido {jugador}, ganó usted")
        
    if resultado == 1:
        victorias_maq += 1
    elif resultado == 0:
        empates += 1
    else: 
        victorias_jug += 1


    print(
        f"""
        La tabla va de la siguiente manera:
        Máquina = {victorias_maq}
        Jugador = {victorias_jug}
        Empates = {empates}
        """
    )