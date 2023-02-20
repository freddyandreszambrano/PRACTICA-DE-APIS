from pprint import pprint
import json

archivo = open("publicacion.json")
contenido_json = json.load(archivo)
nombres = []
ppp = []


def principal():
    cantidad_de_profes= 0
    # ciclo para saber cual es la cantidad de publicaciones por profesor#
    for profes in contenido_json:
        publi = 0
        areas_t = ""
        cientificas = 0
        regionales = 0
        cedula = profes["cedula"]
        name = profes["apellidos"]
        publicacion = {
            "1-nombre": name,
            "2-cedula": cedula,
            "3-publicaciones": 0,
            "4-areas trabajadas": "",
            "5-bases cientificas": 0,
            "6-bases regionales": 0

        }
        for indi in contenido_json:
            if cedula == indi["cedula"]:
                publi += 1
                if indi["area"] not in areas_t:
                    areas_t += indi["area"]
                if indi["tipobases"] == "CIENTIFICAS":
                    cientificas += 1
                if indi["tipobases"] == "REGIONALES":
                    regionales += 1


        publicacion["3-publicaciones"] = publi
        publicacion["4-areas trabajadas"] = areas_t
        publicacion["5-bases cientificas"] = cientificas
        publicacion["6-bases regionales"] = regionales
        if publicacion not in ppp:
            cantidad_de_profes += 1
            ppp.append(publicacion)
    pprint(ppp)
    print(f"la cantidad de profesores son {cantidad_de_profes}")


if __name__ == "__main__":
    principal();
