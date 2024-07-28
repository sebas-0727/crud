from flask import Flask
from flask_cors import CORS
from avistamiento import avistamiento_blueprint
from mapa import mapa_blueprint
from diagrama import diagrama_blueprint
from avistador import avistador_blueprint

app = Flask(__name__)
CORS(app)


app.register_blueprint(avistamiento_blueprint)#avistamiento
app.register_blueprint(avistador_blueprint)#avistador
app.register_blueprint(mapa_blueprint)#mapa
app.register_blueprint(diagrama_blueprint)#diagrama


if __name__ == '__main__':
    
    app.run(debug=True ,port=3306,use_reloader=False)