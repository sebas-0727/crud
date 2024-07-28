from flask import Flask, Blueprint, jsonify, request, render_template
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Función para conectar a la base de datos MySQL
def conectar():
    conn = pymysql.connect(host='beztemoivhfz3gme6cg2-mysql.services.clever-cloud.com', user='ueimrvxlppm556x2', passwd='g4RxFIaDLiTjAdDY1DZZ', db='beztemoivhfz3gme6cg2')
    return conn

# Blueprint para avistamientos
avistamiento_blueprint = Blueprint('avistamiento', __name__)

# Ruta para mostrar el formulario
@avistamiento_blueprint.route("/avistamiento")
def formulario_avistamiento():
    return render_template("avistamiento.html")

# Ruta para registrar un avistamiento
@avistamiento_blueprint.route("/registrar_avistamiento", methods=['POST'])
def registrar_avistamiento():
    try:
        conn = conectar()
        cur = conn.cursor()
        sql = "INSERT INTO avistamiento (ubicacion, hora, aspecto, ataco, imagen) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (request.json['ubicacion'], str(request.json['hora']), request.json['aspecto'], request.json['ataco'], request.json['imagen']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Avistamiento agregado correctamente'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al agregar avistamiento'})

# Ruta para consultar todos los avistamientos
@avistamiento_blueprint.route("/avistamientos_general", methods=['GET'])
def consultar_avistamientos():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT numero, ubicacion, hora, aspecto, ataco, imagen FROM avistamiento")
        data = [{'numero': row[0], 'ubicacion': row[1], 'hora': str(row[2]), 'aspecto': row[3], 'ataco': row[4], 'imagen': row[5]} for row in cur.fetchall()]
        cur.close()
        conn.close()
        return jsonify({'avistamientos': data, 'mensaje': 'Avistamientos en la zona'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al consultar avistamientos'})

# Ruta para eliminar un avistamiento por número
@avistamiento_blueprint.route("/eliminar_avistamiento/<int:numero>", methods=['DELETE'])
def eliminar_avistamiento(numero):
    try:
        conn = conectar()
        cur = conn.cursor()
        sql = "DELETE FROM avistamiento WHERE numero = %s"
        cur.execute(sql, (numero,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Avistamiento eliminado correctamente'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al eliminar avistamiento'})

# Registro del blueprint
app.register_blueprint(avistamiento_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
