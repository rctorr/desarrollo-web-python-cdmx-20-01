# 1. Imprimir una linea de la tabla
# 2. Repetir el paso 1 para cada una de las líneas de tabla

print("-"*42)
print("{:30} | {:10}".format("RESERVACION", "PRECIO"))
print("-"*42)
print("{:30} | {:10.2f}".format("Habitación doble", 15000.00))
print("{:30} | {:10.2f}".format("Transporte", 3000.00))
print("{:30} | {:10.2f}".format("Reservación en evento", 3999.99))
print("{:30} | {:10.2f}".format("Tour en lancha", 21750.00))
print("{:30} | {:10.2f}".format("Alimentos y bebidas", 5000.00))
print("-"*42)
print("{:>30} | {:10.2f}".format("Total", 164170.99))
