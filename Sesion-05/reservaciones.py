# 1. Leer archivo csv
# 1.1  Leer cada fila y guardarla como objeto Servicio()
# 1.2  Regresar una lista de objetos de tipo Servicio
# 2. Imprimir la lista en formato interno de python
import csv

class Servicio:
    def __init__(self, id_servicio, concepto, cantidad, precio):
        """ Inicializa el objeto Servicio """
        self.id = id_servicio
        self.concepto = concepto
        self.cantidad = cantidad
        self.precio = precio
        
    def __str__(self):
        """ Representación impresa de Servicio """
        return self.concepto


def lee_csv(nomarch):
    """
    Lee los registro de nomarch y regresa como lista de servicios
    """
    with open(nomarch, encoding="utf-8") as da:
        da_csv = csv.reader(da)
        encabezado = next(da_csv)
        # ["ID", "CONCEPTO", "CANTIDAD", "PRECIO"]
        servicios = []
        for fila in da_csv:
            # ["1", "alimentos y bebidas", "1", "1000.00"]
            id_servicio = int(fila[0])
            concepto = fila[1]
            cantidad = int(fila[2])
            precio = float(fila[3])
            
            servicio = Servicio(
                id_servicio, concepto, cantidad, precio)
            
            servicios.append(servicio)
            
    return servicios        

def main():
    """ función principal del script """
    nomarch = "reservaciones.csv"
    
    lista_de_servicios = lee_csv(nomarch)
    
    for servicio in lista_de_servicios:
        print(servicio.id, servicio)

if __name__ == "__main__":
    main()