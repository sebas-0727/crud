from flask import Flask, Blueprint, jsonify, request
from flask_cors import CORS
import pymysql

app = Flask(__name__)
CORS(app)

# Función para conectar a la base de datos MySQL
def conectar():
    conn = pymysql.connect(host='beztemoivhfz3gme6cg2-mysql.services.clever-cloud.com', user='ueimrvxlppm556x2', passwd='g4RxFIaDLiTjAdDY1DZZ', db='beztemoivhfz3gme6cg2')
    return conn

# Blueprint para mapa
mapa_blueprint = Blueprint('mapa', __name__)

@mapa_blueprint.route("/mapa", methods=['POST'])
def registro():
    try:
        conn = conectar()
        cur = conn.cursor()
        sql = "INSERT INTO mapa (cordenada, nombre, color, veneno) VALUES (%s, %s, %s, %s)"
        cur.execute(sql, (request.json['cordenada'], request.json['nombre'], request.json['color'], request.json['veneno']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Información del mapa registrada correctamente'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al registrar información del mapa'})

@mapa_blueprint.route("/mapa_general", methods=['GET'])
def consulta_general():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT cordenada, nombre, color, veneno FROM mapa")
        data = [{'cordenada': row[0], 'nombre': row[1], 'color': row[2], 'veneno': row[3]} for row in cur.fetchall()]
        cur.close()
        conn.close()
        return jsonify({'mapa': data, 'mensaje': 'Información del mapa'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al consultar información del mapa'})

# Registro del blueprint en la aplicación Flask
app.register_blueprint(mapa_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
