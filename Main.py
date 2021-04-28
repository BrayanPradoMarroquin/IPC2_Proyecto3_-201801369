from flask import Flask, redirect, render_template, request, Response
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resourse={r"/*": {"origin": "*"}})

@app.route('/events/', methods=['POST'])
def post_events():
    data = open('data.txt', 'w+')
    data.write(request.data.decode('utf-8'))
    data.close()

    return Response(response=request.data.decode('utf-8'),
                    mimetype='text/plain',
                    content_type='text/plain')

@app.route('/events/', methods=['GET'])
def get_evets():
    data = open('data.txt', 'r+')
    return Response(response=data.read(),
                    mimetype='text/plain',
                    content_type='text/plain')

if __name__ == '__main__':
    #app.run(threaded=True,port=5000)
    app.run(debug=True, port=5000)