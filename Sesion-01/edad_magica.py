import random

# 1. Leer nombre de usuaro
nombre = input("Dame tu nombre:")
# 2. Cambiar el nombre a mayúsculas
nombre = nombre.upper()
# 3. Imprimir saludo con el nombre
print("Hola", nombre)
# 4. Adivinar la edad del usuario
edad = random.randint(3, 120)
# 5. Imprimir la edad del usuario
# print("Tu edad real es", edad, "años")
print("Tu edad real es {} años".format(edad))