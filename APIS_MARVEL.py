import requests
import json
from pprint import pprint
ts = 1
priavate_key = "7a2c5dac90465938a24c4350b99bc825be465b06"
public_key = "1d7bc842e2779337c49d6785e0dc27a6"

#17a2c5dac90465938a24c4350b99bc825be465b061d7bc842e2779337c49d6785e0dc27a6

hashed = "a6b8206b37282739f67d2e73b912870b"
url =f"https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={public_key}&hash={hashed}"
lista = []
respuesta = requests.get(url)
if respuesta.status_code == 200:
    respuesta_json= json.loads(respuesta.text)
    #pprint(respuesta_json)

    for index in respuesta_json["data"]["results"]:
        nombre = index["name"]
        descripcion = index["description"]
        comics_disponibles = index["comics"]["available"]
        series_disponibles = index["series"]["available"]
        dict= {"nombre": nombre, "descripcion": descripcion,"comic disponibles": comics_disponibles,"series disponibles": series_disponibles }
        lista.append(dict)
        pprint(lista)
        print("*************************")

    #pprint(lista)