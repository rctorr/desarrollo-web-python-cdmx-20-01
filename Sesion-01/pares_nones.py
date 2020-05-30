# 1. Leer el valor de N
cad = input("Dame un número entero mayor que cero:")
n = int(cad)
# 2. Generar una lista de N números
lista = range(n)
# 3. Determinar cuales son pares y nones y asignar la palabra correcta
# 4. Imprimir el resultado
for i in lista:
    if i % 2 == 0:  # par
        print(i, "par")
    else:
        print(i, "impar")

