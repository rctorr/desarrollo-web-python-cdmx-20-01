import click
import csv

# 1. Generar la lista de conceptos en una lista de diccionarios
# 2. Agregar el campo calculado de subtotal.
# 3. Imprimir la tabla de la reservación.


def obtiene_conceptos(nomarch):
    """
    Obtiene la lista de comceptos de una reservación desde nomarch
    """
    # Se lee todas las fila de un sólo golpe
    with open(nomarch) as da:
        da_csv = csv.DictReader(da)
        encabezados = da_csv.fieldnames
        conceptos = list(da_csv)
        
    # Se realiza conversión de tipos de datos
    for concepto in conceptos:
        concepto["CANTIDAD"] = int(concepto["CANTIDAD"])
        concepto["PRECIO"] = float(concepto["PRECIO"])
        
    return encabezados, conceptos


def imprime_txt(conceptos, total, encabezados):
    """ Imprime en formato txt la lista de conceptos """
    # Imprimiendo tabla
    linea = "-" * 70
    formato1 = "{:30} | {:8} | {:10} | {:10}"  # Encabezado
    formato2 = "{:30} | {:8} | {:10.2f} | {:10.2f}"  # Para los conceptos
    formato3 = "{:30} | {:8} | {:>10} | {:10.2f}"  # Para el total

    print(linea)
    print(formato1.format(*encabezados))
    print(linea)
    for c in conceptos:
        print(formato2.format(*c.values()))
    print(linea)
    print(formato3.format("", "", "Total", total))

    
def imprime_html(conceptos, total, encabezados):
    """ Imprime en formato HTML la lista de conceptos """
    # Imprimiendo tabla
    formato1 = "<tr><th>{}</th><th>{}</th><th>{}</th><th>{}</th></tr>"
    formato2 = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>"  # Para los conceptos

    print("<table>")
    print( formato1.format(*encabezados) )
    for c in conceptos:
        print( formato2.format(*c.values()) )
    print(formato2.format("", "", "Total", total))
    print("</table>")


@click.command()
@click.option("--html", "es_html", is_flag=True,
    help="Imprime el resultado en formato HTML")
def main(es_html):
    """ Imprime la lista de conceptos de una reservación """
    nomarch = "reservaciones.csv"
    
    # Llamamos a la función y guardamos el valor que regresa
    encabezados, conceptos = obtiene_conceptos(nomarch)
    # Se calcula y agrega la columna de subtotal y de paso el total
    encabezados.append("SUBTOTAL")
    total = 0
    for c in conceptos:  # c -> diccionario
        c["SUBTOTAL"] = c["CANTIDAD"] * c["PRECIO"]
        total += c["SUBTOTAL"]

    # Ordenamiento por nombre de concepto
    conceptos.sort(key=lambda x: x["PRODUCTO"].lower())
    
    if es_html:
        imprime_html(conceptos, total)
    else:
        imprime_txt(conceptos, total, encabezados)

if __name__  == "__main__":
    # Si __name__ es igual al valor "__main__" el script se ejecuta
    # desde la línea de comando y tenemos que ejecutar la función
    # main()
    main()