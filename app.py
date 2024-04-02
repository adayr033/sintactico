from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola bienvenido!'

if __name__ == '_main_':
  app.run(host='0.0.0.0', port=80)