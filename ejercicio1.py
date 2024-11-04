from AVL import ARBOLAVL

# 1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenada
# de los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir
# tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente:

# a) los índices de cada uno de los árboles deben ser nombre, número y tipo;

# b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este
# último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben
# mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos
# caracteres–;

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;

# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y
# además un listado por nivel por nombre;

# e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum;

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero.

print("")
print("Resolucion")
print("")

#A

#armamos los arboles

arbolnombre = ARBOLAVL()
arbolnumero = ARBOLAVL()
arboltipo = ARBOLAVL()

#diccionario con los pokemones

pokemones = [
    {"nombre": "Bulbasaur", "numero": 1, "tipos": ["planta", "veneno"]},
    {"nombre": "Charmander", "numero": 4, "tipos": ["fuego"]},
    {"nombre": "Squirtle", "numero": 7, "tipos": ["agua"]},
    {"nombre": "Pikachu", "numero": 25, "tipos": ["eléctrico"]},
    {"nombre": "Jolteon", "numero": 135, "tipos": ["eléctrico"]},
    {"nombre": "Lycanroc", "numero": 745, "tipos": ["roca"]},
    {"nombre": "Tyrantrum", "numero": 697, "tipos": ["roca", "dragón"]},
    {"nombre": "Lukelzi", "numero": 62, "tipos": ["acero"]},
]

#carga de los pokemones en los arboles

for pokemon in pokemones:
    arbolnombre.insert_node(pokemon['nombre'],other_value=pokemon)
    arbolnumero.insert_node(pokemon['numero'],other_value=pokemon)
    for tipo in pokemon['tipos']:
        arboltipo.insert_node(tipo, other_value=pokemon)

#B

#para buscar vamos a hacer una funcion

print("")
print("Punto B: ")

def buscarnombre(nombre):
    resultado = []
    busqueda = arbolnombre.proximity_search(nombre)
    if busqueda is not None:
        resultado.append(busqueda.other_value)
    else:
        print("No se encontro el pokemon")
    return resultado

#si lo encuentra lo agrega a resultado y luego lo imprimimos 

print("Pokémon que contienen 'bul':", buscarnombre("Bul"))

#C

#creamos uan funcion que busca por el tipo del pokemon
print("")
print("Punto C: ")

def listartipo(tipo):
    resultado = []
    busqueda = arboltipo.search(tipo)
    if busqueda:
        def listaportipo(root):
            if root is not None:
                if tipo in root.other_value["tipos"]:
                    resultado.append(root.other_value["nombre"])
                #llamadas recursivas para terminar de recorrer los arboles
                listaportipo(root.left)
                listaportipo(root.right)
        listaportipo(busqueda)
    return resultado


print("Pokémon de tipo agua:", listartipo("agua"))
print("Pokémon de tipo fuego:", listartipo("fuego"))
print("Pokémon de tipo planta:", listartipo("planta"))
print("Pokémon de tipo electrico:", listartipo("eléctrico"))

#D
print("")
print("Punto D: ")


#hacemos listado ascendente con inorden
print("Listado ascendente por numero: ")
arbolnumero.inorden()
print("")
print("Listado ascendente por nombre: ")
arbolnombre.inorden()
print("")
#y con bylevel nos imprime el nivel del arbol con su respectivo nombre
print("Listado por niveles por nombre: ")
arbolnombre.by_level()

print

#E

#vamos a utilizar la funcion del punto b
print("")
print("Punto E: ")

print("Pokemones requeridos: ")
print("Pokemon 1", buscarnombre("Jolteon"))
print("Pokémon 2", buscarnombre("Lycanroc"))
print("Pokémon 3", buscarnombre("Tyrantrum"))

#F

print("")
print("Punto F: ")

#ahora vamos a determinar cuanto pokemones hay de tipo electrico y acero

def busquedaf(tipo):
    sumatipos = 0
    busqueda = arboltipo.search(tipo)
    if busqueda:
        def sumatotal(root):
            nonlocal sumatipos
            if root is not None:
                if tipo in root.other_value["tipos"]:
                    sumatipos += 1
                # llamadas recursivas para recorrer el árbol
                sumatotal(root.left)
                sumatotal(root.right)
        sumatotal(busqueda)
    return sumatipos
#en esta parte si coincide el tipo sumamos a la variable y despues la imprimimos
print("Pokemones tipo Electrico : ", busquedaf("eléctrico"))
print("")
print("Pokemones tipo Acero : ", busquedaf("acero"))


