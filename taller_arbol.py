import json

class Nodos():

	def __init__(self, id, nombre):
		self.id = id
		self.nombre = nombre
		self.hijo1 = None
		self.hijo2 = None

def crear_arbol(json):
	nodos = {}
	for i in range(len(json["personas"])):
		nodos[i] = Nodos(json["personas"][i]["id"], json["personas"][i]["nombre"])
	for i in range (len(json["padres"])):
		for j in range(len(nodos)):
			if nodos[j].id == json["padres"][i]["padre"]:
				if nodos[j].hijo1 == None:
					nodos[j].hijo1 == nodos[str(json["padres"][i]["hijo"])]
				else:
					nodos[j].hijo2 == nodos[str(json["padres"][i]["hijo"])]
		
with open("arbol_genealogico.json", "r") as file:
	arbol = json.load(file)

crear_arbol(arbol)
