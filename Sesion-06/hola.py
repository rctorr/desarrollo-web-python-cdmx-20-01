from bottle import route, run, template

@route('/hola/<nombre>')
def index(nombre):
    return template('<b>Hola como estás {{nombre}}</b>!', nombre=nombre)

run(host='localhost', port=8080)