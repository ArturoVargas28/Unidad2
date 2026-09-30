'''
Mi primer servidor web con Flask y Python
Autor: Arturo Vargas
Fecha: 30 De Septiembre 2026
'''

from flask import Flask
app = Flask(__name__)

inventario = [
	{"hostname": "Core-SW01", "ip": "10.0.0.1", "status": "up"}, 
	{"hostname": "Dist-SW02", "ip": "10.0.0.2", "status": "down"}, 
	{"hostname": "Access-SW03", "ip": "10.0.0.3", "status": "up"}, 
	{"hostname": "Edge-R01", "ip": "172.16.1.1", "status": "down"} 
]

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route('/<nombre>')
def saludo(nombre):
	return f"Hola {nombre}</h1>"


@app.route('/dispositivo/<device>')
def buscar_dispositivo(device):
	return f"{device}"


@app.route('/dispositivo/<device>')
def buscar_dispositivos(device):
    for equipo in inventario:
        if equipo["hostname"] == device:
            return equipo["status"]
    return "No encontrado"

if __name__ == "__main__":
	app.run(debug=True, port=5015)