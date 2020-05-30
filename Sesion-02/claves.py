# 1. Leer el valor de n desde el usuario
# 2. Leer el valor de m desde el usuario
# 3. Crea o construir una contraseña
# 4. Imprimir la contraseña
# --
# 5. Resolver para generar N claves

import random


def lee_entero(msg):
    """ Lee un número entero desde el usuario """
    es_entero = False
    while not es_entero:
        resp = input(msg)
        if resp.isdigit():
            n = int(resp)
            es_entero = True
        else:
            print("Error: El valor proporcionado no es un entero")

    return n

n = lee_entero("Número de claves a generar N= ")
m = lee_entero("Longitud de las claves M= ")

# Construyendo una contraseña
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()
digitos = "1234567890"
alfabeto = minusculas + mayusculas + digitos

for j in range(n):
    clave = ""
    clave = clave + random.choice(minusculas)  # clave -> "g"
    clave = clave + random.choice(minusculas)  # clave -> "g"
    clave += random.choice(mayusculas)  # clave -> "gT"
    clave += random.choice(digitos)  # clave -> "gT7"

    # Los símbolos que falta de la clave
    p = m - 4  # m=10 -> p = 10 - 3 = 7
    for i in range(p):
        clave += random.choice(alfabeto)

    # Desornedar la contraseña
    letras = random.sample(clave, m)
    clave = "".join(letras)

    print(clave)