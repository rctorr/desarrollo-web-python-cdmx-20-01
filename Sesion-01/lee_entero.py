es_entero = False
while not es_entero:  # not False => True
    # 1. Lee una respuesta del usuario (str)
    resp = input("Dame un número entero: ")
       # "56", "56.0", "56e2", "cinco"
       # ¿si la cadena de texto tiene sólo digitos "1234567890", entonces un entero?

    # 1.5 Verificar que la respuesta sea un número entero
    # 2. Convertir la respuesta a numero
    # 3. Si la conversión es correcta se imprime el número y fin.
    if resp.isdigit():
        n = int(resp)
        es_entero = True
    else:
        print("Error: El valor proporcinado no es un entero")


    # 4. Si la conversión no es correcta, imprimer error y solicitar nueva respuesta

print("El entero es:", n)