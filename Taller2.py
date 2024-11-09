#Primer ejercicio
import math
import statistics


Empleados = [
    {
        "nombre":"Nixon",
        "horas laborales":20,
        "horas nocturnas":4
    },
    {
        "nombre":"James",
        "horas laborales":50,
        "horas nocturnas":2
    },
    {
        "nombre":"Son",
        "horas laborales":30,
        "horas nocturnas":24
    },
    {
        "nombre":"Karim",
        "horas laborales":10,
        "horas nocturnas":5
    }
]

Empleados.append(
    {
    "nombre":"Sonni",
    "horas laborales": 34,
    "horas nocturnas": 21
    }
)

print(Empleados)


#ejercicio2

print("BIENVENIDO AL GYM")

nombre= input("Por favor ingrese su nomnre: ")
horas_mes = int(input(f"Hola {nombre}, ingresa por favor le número de horas entrenadas este mes: "))

valor1= 5000
valor2=3500
valor3=2000


if horas_mes <= 15:
    print(f"Su clasificación es Bronce, y deberá pagar el valor de {horas_mes*valor1}")
elif horas_mes <=30:
    print(f"Su clasificación es Plata, y deberá pagar el valor de {horas_mes*valor2}")
else:
    print(f"Su clasificación es Oro, y deberá pagar el valor de {horas_mes*valor3}")

#ejercicio3

nombre_1 = input("Ingresa su nombre: ")
nota1 = float(input(f"Hola {nombre_1}, ingresa ahora la nota de la primer evalaución: "))
nota2 = float(input(f"Hola {nombre_1}, ingresa ahora la nota de la segunda evalaución: "))
nota3 = float(input(f"Hola {nombre_1}, ingresa ahora la nota de la tercer evalaución: "))

notas= [
    nota1, nota2, nota3
]
promedio= statistics.mean(notas)


if 90 <= promedio <= 100:
    print(f"Hola {nombre_1} Su clificación es {promedio} por lo tanto es superior")
elif 80 <= promedio <= 89:
    print(f"Hola {nombre_1} Su clificación es {promedio} por lo tanto es alto")
elif 70 <= promedio <= 79:
    print(f"Hola {nombre_1} Su clificación es {promedio} por lo tanto es básico")
elif 60 <= promedio <= 69:
    print(f"Hola {nombre_1} Su clificación es {promedio} por lo tanto es bajo")
elif 0 <= promedio <= 59:
    print(f"Hola {nombre_1} Su clificación es {promedio} por lo tanto es insuficiente")
