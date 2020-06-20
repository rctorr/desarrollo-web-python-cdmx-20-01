from bottle import route, run, template

from reservacion import lee_csv

@route('/reservacion/<id>')
def index(id):
    
    nomarch = "reservaciones.csv"
    id = int(id)
    
    consumos = lee_csv(nomarch)
    consumos_id = [
        consumo for consumo in consumos if consumo.id == id]
    
    plantilla = """
    <html>
    <body>
      <h3>Lista de conceptos de la reservación número {{id}}</h3>
      <hr />
      <table>
        <tr><th>ID</th><th>CONCEPTO</th><th>CANTIDAD</th>
        <th>PRECIO</th></tr>
        {{filas}}
      </table>
    </body>
    </html>
    """
    
    formato1 = "<tr><td>{}</td><td>{}</td><td>{}</td><td>{}</td></tr>"
    lista_filas = []
    for consumo in consumos_id:
        fila = formato1.format(*consumo.tupla())
        lista_filas.append(fila)
    lista_filas_txt = "\n".join(lista_filas)
    plantilla = plantilla.replace("{{filas}}", lista_filas_txt)
    
    return template(plantilla, id=id)


@route('/json/<id:int>')
def reservacion_json(id):
    """ Responde a la petición GET /json/<id> """

    # Obtener lista de consumos en base al id desde el archivo csv
    nomarch = "reservaciones.csv"
    consumos = lee_csv(nomarch)
    consumos_id = [
        consumo for consumo in consumos if consumo.id == id]
    
    # Armando la reservacion en diccionario
    reservacion_dict = {
        "ID" : id,
        "CONSUMOS" : []
    }
    for consumo in consumos_id:
        consumo_dict = {
            "id" : consumo.id,
            "concepto" : consumo.concepto,
            "cantidad" : consumo.cantidad,
            "precio" : consumo.precio
        }
        reservacion_dict["CONSUMOS"].append(consumo_dict)

    return reservacion_dict


run(host='localhost', port=8080, reloader=True)