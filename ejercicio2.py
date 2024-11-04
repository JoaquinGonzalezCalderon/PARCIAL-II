from grafo import Graph

# 2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los
# algoritmos necesarios para resolver las siguientes tareas:

# a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la
# cantidad de episodios en los que aparecieron juntos ambos personajes que se
# relacionan;

# b) hallar el árbol de expansión minino y determinar si contiene a Yoda;

# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 

# d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, 
# Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.

grafoSW = Graph(dirigido=False)

#A - insertamos los vertices

personajes = ["Luke Skywalker", "Darth Vader", "Yoda", "Boba Fett", "C-3PO", "Leia", 
              "Rey", "Kylo Ren", "Chewbacca", "Han Solo", "R2-D2", "BB-8"]
for personaje in personajes:
    grafoSW.insert_vertice(personaje)

#y ahora las aristas

grafoSW.insert_arista("Luke Skywalker", "Darth Vader", 4)
grafoSW.insert_arista("Luke Skywalker", "Leia", 5)
grafoSW.insert_arista("Luke Skywalker", "Yoda", 3)
grafoSW.insert_arista("Luke Skywalker", "Han Solo", 4)
grafoSW.insert_arista("Luke Skywalker", "C-3PO", 5)
grafoSW.insert_arista("Luke Skywalker", "R2-D2", 5)
grafoSW.insert_arista("Darth Vader", "Leia", 2)
grafoSW.insert_arista("Darth Vader", "Yoda", 1)
grafoSW.insert_arista("Darth Vader", "Boba Fett", 2)
grafoSW.insert_arista("Leia", "Han Solo", 5)
grafoSW.insert_arista("Leia", "C-3PO", 5)
grafoSW.insert_arista("Leia", "R2-D2", 5)
grafoSW.insert_arista("Han Solo", "Chewbacca", 6)
grafoSW.insert_arista("Han Solo", "C-3PO", 4)
grafoSW.insert_arista("Han Solo", "R2-D2", 4)
grafoSW.insert_arista("C-3PO", "R2-D2", 6)
grafoSW.insert_arista("Yoda", "Chewbacca", 2)
grafoSW.insert_arista("Yoda", "Rey", 1)
grafoSW.insert_arista("Rey", "Kylo Ren", 3)
grafoSW.insert_arista("Rey", "BB-8", 3)
grafoSW.insert_arista("Kylo Ren", "BB-8", 1)
grafoSW.insert_arista("Kylo Ren", "Darth Vader", 1)
grafoSW.insert_arista("Chewbacca", "R2-D2", 3)
grafoSW.insert_arista("Chewbacca", "Leia", 4)

#B
print("Punto B: ")
#usamos kruskal para el arbol de expansion minima
grafoexpansionminima = grafoSW.kruskal("Luke Skywalker")
#y aca verificamos si tiene a yoda
for arista in grafoexpansionminima:
    if "Yoda" in arista:
        print(f"Yoda está en el árbol de expansión mínima")
    else:
        print(f"Yoda no está en el árbol de expansión mínima")
print("")
print("Grafo de Expansion Minima: ",grafoexpansionminima)
print("")

#C
print("Punto C: ")
episodiosmaximo = 0
parpersonajes = None
#ahora vemos nodo x nodo para ver los personajes y recopilar el maximo
for nodo in grafoSW.elements:
    for aristas in nodo['aristas']:
        if aristas['peso'] > episodiosmaximo:
            episodiosmaximo = aristas['peso']
            parpersonajes = (nodo['value'], aristas['value'])

print("Máximo número de episodios compartidos:", episodiosmaximo)
print("")
print("Personajes que los comparten:", parpersonajes)
print("")
