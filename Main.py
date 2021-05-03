from flask import Flask, redirect, render_template, request, Response
from flask_cors import CORS
import base64
from fronted.web import EntradasXML as xml

salida=None
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
    global salida
    salida=""
    datos = request.get_json()
    if datos['data'] == '':
        return {"msg": 'Error en contenido'}
    contenido = base64.b64decode(datos['data']).decode('utf-8')
    salida=contenido
    print(salida)
    #xml.AbrirArchivo(salida)
    return salida

@app.route('/abrirArchivo', methods=['GET'])
def get_events():
    global salida
    data = salida
    return Response(response=data,
                    mimetype='text/plain',
                    content_type='text/plain')

if __name__ == '__main__':
    #app.run(threaded=True,port=5000)
    app.run(debug=True)