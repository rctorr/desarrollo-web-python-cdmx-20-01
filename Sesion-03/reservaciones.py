import click

# 1. Generar la lista de conceptos en una lista de diccionarios
# 2. Agregar el campo calculado de subtotal.
# 3. Imprimir la tabla de la reservación.


def obtiene_conceptos():
    """ Obtiene la lista de comceptos de una reservación """
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
    
    return conceptos


def imprime_txt(conceptos, total):
    """ Imprime en formato txt la lista de conceptos """
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

    
def imprime_html(conceptos, total):
    """ Imprime en formato HTML la lista de conceptos """
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


@click.command()
@click.option("--html", "es_html", is_flag=True,
    help="Imprime el resultado en formato HTML")
def main(es_html):
    """ Imprime la lista de conceptos de una reservación """
    
    # Llamamos a la función y guardamos el valor que regresa
    conceptos = obtiene_conceptos()
    # Calcular el campo de subtotal y total
    total = 0
    for c in conceptos:  # c -> diccionario
        c["SUBTOTAL"] = c["CANTIDAD"] * c["PRECIO"]

    # Ordenamiento por nombre de concepto
    conceptos.sort(key=lambda x: x["CONCEPTO"].lower())
    
    if es_html:
        imprime_html(conceptos, total)
    else:
        imprime_txt(conceptos, total)

if __name__  == "__main__":
    # Si __name__ es igual al valor "__main__" el script se ejecuta
    # desde la línea de comando y tenemos que ejecutar la función
    # main()
    main()