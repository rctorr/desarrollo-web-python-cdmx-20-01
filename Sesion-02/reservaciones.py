# 1. Generar la lista de conceptos en una lista de diccionarios
# 2. Agregar el campo calculado de subtotal.
# 3. Imprimir la tabla de la reservación.

conceptos = [
    {
        "CONCEPTO":"Habitación doble",
        "CANTIDAD":1,
        "PRECIO":15000.00
    },
    {
        "CONCEPTO":"Transporte",
        "CANTIDAD":3,
        "PRECIO":3000.00
    },
    {
        "CONCEPTO":"Reservación en evento",
        "CANTIDAD":1,
        "PRECIO":3999.99
    }
]

# Agregando un sólo concepto a la lista
concepto = {
    "CONCEPTO":"Tour en lancha",
    "CANTIDAD":2,
    "PRECIO":2175.00
}
conceptos.append(concepto)

# Agregando otro concepto a la lista
concepto = {
    "CONCEPTO":"alimentos y bebidas",
    "CANTIDAD":1,
    "PRECIO":5000.00
}
conceptos.append(concepto)

# Calcular el campo de subtotal y total
total = 0
for c in conceptos:  # c -> diccionario
    c["SUBTOTAL"] = c["CANTIDAD"] * c["PRECIO"]
    
# Imprimiendo tabla
linea = "-" * 70
formato1 = "{:30} | {:8} | {:10} | {:10}"  # Encabezado
formato2 = "{:30} | {:8} | {:10.2f} | {:10.2f}"  # Para los conceptos
formato3 = "{:30} | {:8} | {:>10} | {:10.2f}"  # Para el total

print(linea)
print(formato1.format("CONCEPTO", "CANTIDAD", "PRECIO", "SUBTOTAL"))
print(linea)
for c in conceptos:
    print(formato2.format(
        c["CONCEPTO"], c["CANTIDAD"], c["PRECIO"], c["SUBTOTAL"]))
print(linea)
print(formato3.format("", "", "Total", total))
