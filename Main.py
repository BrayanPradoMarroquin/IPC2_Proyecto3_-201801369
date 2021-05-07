from flask import Flask, redirect, render_template, request, Response
from flask_cors import CORS
import base64
import EntradasXML as xml

salida=None
alterado=None
app = Flask(__name__)
cors = CORS(app, resourse={r"/*": {"origin": "*"}})

@app.route('/')
def init():
    return redirect('inicio')

@app.route('/inicio')
def inicio():
    return render_template('Inicio.html')

@app.route('/abrirArchivo', methods=['POST'])
def abrirArchivo():
    global salida, alterado
    salida=""
    datos = request.get_json()
    if datos['data'] == '':
        return {"msg": 'Error en contenido'}
    contenido = base64.b64decode(datos['data']).decode('utf-8')
    salida=contenido
    print(salida)
    alterado = xml.AbrirArchivo(salida)
    return salida

@app.route('/abrirArchivo', methods=['GET'])
def get_events():
    global alterado
    data = alterado
    return Response(response=data,
                    mimetype='text/plain',
                    content_type='text/plain')

@app.route('/llamarxml', methods=['GET'])
def llamar():

    archivoentrante = open('estadistica.xml', 'r')
    lecturaxml = archivoentrante.read()

    return Response(lecturaxml, mimetype='text/xml')

if __name__ == '__main__':
    #app.run(threaded=True,port=5000)
    app.run(debug=True)