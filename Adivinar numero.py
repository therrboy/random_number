from random import randint

juego = True
print("Bienvenido al juego, pienso en un numero del 1 al 100")
dificultad = str(input("Que dificultad prefieres? Facil o Dificil? ").lower())
dificultad_valores = {
    "dificil": 5,
    "facil": 10
}
print(f"Tienes {dificultad_valores[dificultad]} intentos ")

intentos = dificultad_valores[dificultad]
numero_random = randint(1, 100)
eleccion = 0

def repeticion(eleccion, intentos, numero_random):
    while numero_random != eleccion:
        eleccion = int(input("Por favor introduce el primer numero que prefieras "))
        intentos -= 1
        if intentos > 0:
            if eleccion == numero_random:
                print("Correcto adivinaste!")
            elif eleccion > numero_random:
                print("Te pasaste! es un numero mas chico")
            elif eleccion < numero_random:
                print("Te quedaste corto! es un numero mas grande")
        else:
            print("Perdiste, te quedaste sin intentos")

repeticion(eleccion, intentos, numero_random)