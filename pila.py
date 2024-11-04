class Stack:

    # Todas las clases deben tener uno o mas metodos constructores, que permiten crear objetos a partir
    # de una clase.

    def __init__(self):
        self.__elements = []

    def push(self, element):
        self.__elements.append(element)

    def pop(self):
        if len(self.__elements) > 0:
            return (
                self.__elements.pop()
            )  # Con el return devuelve el valor que se saca de la pila
        else:
            return None

    def on_top(self):
        if len(self.__elements) > 0:
            return self.__elements[-1]
        else:
            return None

    def size(self):
        return len(self.__elements)


# from random import randint

# pila = Stack()
# pila_aux = Stack()

# #Le da 10 elementos random entre el 1 y el 99

# for i in range(10):
#     pila.push(randint(1,99))


# print(pila.on_top())
# print(pila.size())

# # Listado

# while pila.size() > 0:
#     data = pila.pop()
#     print(data)
#     pila_aux.push(data)

# print()

# # Reconstruccion

# while pila_aux.size()>0:
#     pila.push(pila_aux.pop())

# Primero lo saca con el pop y lo agrega a la pila original con el push

# Sirve para busqueda en pila utilizando un barrido, sin poder perder elementos.
