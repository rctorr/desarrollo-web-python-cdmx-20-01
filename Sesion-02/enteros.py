# 1. Leer el número N desde el usuario
es_entero = False
while not es_entero:
    resp = input("Dame un número entero N: ")
    if resp.isdigit():
        n = int(resp)
        es_entero = True
    else:
        print("Error: El valor proporcinado no es un entero")

# 2. Generar la lista de números desde 0 a N-1
enteros = []
for i in range(n):
    enteros.append(i)
# enteros = [0, 1, 2, 3, 4, ...., N-1]

# 3. Imprimir la lista de números
for j in enteros:
    print(j)