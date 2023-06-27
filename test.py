# import requests 

# BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "hello")
# print(response.json())
import requests
import json

url = 'http://127.0.0.1:5000/question'  # Reemplaza con la URL de tu servidor Flask

# Datos JSON que deseas enviar en el cuerpo de la petición
data = {
    'question': 'pregunta'
}

# Convertir los datos a formato JSON
json_data = json.dumps(data)

# Especificar las cabeceras con el tipo de contenido JSON
headers = {'Content-Type': 'application/json'}

# Realizar la petición POST con los datos JSON y las cabeceras
response = requests.post(url, data=json_data, headers=headers)

# Obtener la respuesta del servidor
respuesta = response.json()

# Imprimir la respuesta
print(respuesta)
