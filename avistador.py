from flask import Flask, Blueprint, jsonify, request, render_template
from flask_cors import CORS
import pymysql

# Configuración de Flask
app = Flask(__name__)
CORS(app)

# Configuración de la conexión a MySQL
def conectar():
    conn = pymysql.connect(host='beztemoivhfz3gme6cg2-mysql.services.clever-cloud.com', user='ueimrvxlppm556x2', passwd='g4RxFIaDLiTjAdDY1DZZ', db='beztemoivhfz3gme6cg2')
    return conn

# Blueprint para avistadores
avistador_blueprint = Blueprint('avistador', __name__)

# Ruta para mostrar el formulario de avistadores
@avistador_blueprint.route("/avistador", methods=['GET'])
def formulario_avistador():
    return render_template("avistador.html")

# Función para registrar un avistador
@avistador_blueprint.route("/registrar_avistador", methods=['POST'])
def registrar_avistador():
    try:
        conn = conectar()
        cur = conn.cursor()
        sql = "INSERT INTO avistador (ficha, nombre) VALUES (%s, %s)"
        cur.execute(sql, (request.json['ficha'], request.json['nombre']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Avistador registrado correctamente'}), 201
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al registrar avistador'}), 500

# Función para consultar todos los avistadores
@avistador_blueprint.route("/avistador_general", methods=['GET'])
def consulta_general():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT id, ficha, nombre FROM avistador")
        data = [{'id': row[0], 'ficha': row[1], 'nombre': row[2]} for row in cur.fetchall()]
        cur.close()
        conn.close()
        return jsonify({'avistadores': data, 'mensaje': 'Avistadores registrados'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al consultar avistadores'}), 500

# Función para actualizar un avistador por su ID
@avistador_blueprint.route("/actualizar_avistador/<int:id>", methods=['PUT'])
def actualizar_avistador(id):
    try:
        conn = conectar()
        cur = conn.cursor()
        sql = "UPDATE avistador SET ficha=%s, nombre=%s WHERE id=%s"
        cur.execute(sql, (request.json['ficha'], request.json['nombre'], id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Avistador actualizado correctamente'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al actualizar avistador'}), 500

# Función para eliminar un avistador por su ID
@avistador_blueprint.route("/eliminar_avistador/<int:id>", methods=['DELETE'])
def eliminar_avistador(id):
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("DELETE FROM avistador WHERE id=%s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'mensaje': 'Avistador eliminado correctamente'})
    except Exception as ex:
        print(ex)
        return jsonify({'mensaje': 'Error al eliminar avistador'}), 500

# Registrar el blueprint de avistadores en la aplicación principal
app.register_blueprint(avistador_blueprint, url_prefix='/avistadores')

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run(debug=True)
