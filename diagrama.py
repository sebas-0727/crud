from flask import Flask
from flask_cors import CORS
from flask import Blueprint, jsonify,request
from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)
## Funcion para conectarnos a la base de datos de mysql
diagrama_blueprint = Blueprint('diagrama',__name__)
def datos_conteo():
    conn = pymysql.connect(
        host='beztemoivhfz3gme6cg2-mysql.services.clever-cloud.com', user='ueimrvxlppm556x2', passwd='g4RxFIaDLiTjAdDY1DZZ', db='beztemoivhfz3gme6cg2'
    )
    consulta = """
    SELECT ubicacion, COUNT(*) AS conteo
    FROM avistamiento
    GROUP BY ubicacion
    """
    cursor = conn.cursor()
    cursor.execute(consulta)
    datos = cursor.fetchall()
    conn.close()
    return datos

# Ruta para la página principal que mostrará el gráfico
@diagrama_blueprint.route("/diagrama",)
def inicio():
    return render_template('diagrama.html')

# Ruta para obtener los datos agrupados con conteo
@diagrama_blueprint.route('/datos')
def datos_json():
    datos = datos_conteo()
    return jsonify(datos)

if __name__ == '__main__':
    app.run(debug=True)
