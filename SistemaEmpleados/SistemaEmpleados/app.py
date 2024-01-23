#Paquetes necesatios: flask, Flask-MySQL, jinja2
#"pip install flask"
#"pip install Flask-MySQL"
#"pip install jinja2"

from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)                                   #creacion de la aplicacion

mysql = MySQL()                                         #declaracion del uso de mysql pasando las instrucciones de la base de datos
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'sistema_empleados'
mysql.init_app(app)                                     #creacion de conexion con los datos

@app.route('/')                                         #pagina principal de la aplicacion
def index():
    query = "INSERT INTO `empleados` (`id_empleado`, `nombre`, `correo`, `foto`) VALUES (NULL, 'Pepe', 'pepito@gmail.com', 'foto.jpg');"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    return render_template('empleados/index.html')      #accede al index.html mediante el render_template

if __name__ == '__main__':                              #codigo que python requiere para empezar a trabajar con la aplicacion
    app.run(debug=True)