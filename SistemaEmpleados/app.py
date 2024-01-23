#Paquetes necesatios: flask, Flask-MySQL, jinja2
#"pip install flask"
#"pip install Flask-MySQL"
#"pip install jinja2"

from flask import Flask
from flask import render_template

app = Flask(__name__)                                   #creacion de la aplicacion

@app.route('/')                                         #pagina principal de la aplicacion
def index():
    return render_template('empleados/index.html')      #accede al index.html mediante el render_template

if __name__ == '__main__':                              #codigo que python requiere para empezar a trabajar con la aplicacion
    app.run(debug=True)