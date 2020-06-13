# 1. Leer el id de la reservacción
# 2. Leer la lista de conceptos desde el archivo csv
# 2.1 Crear un objeto Consumo() por cada concepto
# 2.2 Agregar el objeto creado a una lista
# 3. Filtrar la lista de consumos que coincidan con el id de la reservación.
# 4. Imprimir la lista final
import click
import csv


class Consumo:
    def __init__(self, id, concepto, cantidad, precio):
        """ Función constructora del objeto Consumo """
        self.id = id
        self.concepto = concepto
        self.cantidad = cantidad
        self.precio = precio
        
    def __str__(self):
        """ Regresa la representación en str del objeto """
        return self.concepto


def lee_csv(nomarch):
    """ Lee desde nomarch la lista de consumos """
    with open(nomarch, encoding="utf-8") as da:
        da_csv = csv.reader(da)
        encabezados = next(da_csv)
        lista_consumos = []
        for fila in da_csv:
            # fila -> ["1", "alimentos y bebidas", "1", "5000.00"]
            id = int(fila[0])
            concepto = fila[1]
            cantidad = int(fila[2])
            precio = float(fila[3])
            consumo = Consumo(id, concepto, cantidad, precio)
            lista_consumos.append(consumo)
    
    return lista_consumos


@click.command()
@click.argument("id", type=int)
def main(id):
    """ Imprime los conceptos de la reservación indicada por ID """
    nomarch = "reservaciones.csv"
    
    consumos = lee_csv(nomarch)
    
    # Filtrando consumos por id
    # consumos_id = []
    # for consumo in consumos:
    #    # consumo -> id=1, concepto="alimentos y bebidas", 1, ...
    #    if consumo.id == id:
    #        consumos_id.append(consumo)
    
    # Usando listas de compresión
    consumos_id = [
        consumo for consumo in consumos if consumo.id == id]
    
    # Imprimir
    for consumo in consumos_id:
        print(consumo.id, consumo, consumo.cantidad)


if __name__ == "__main__":
    main()