class Queue:

    def __init__(self):
        self.__elements = []

    def arrive(self, element):
        self.__elements.append(element)

    def atention(self):
        if len(self.__elements) > 0:
            return self.__elements.pop(0)
        else:
            return None

    def size(self):
        return len(self.__elements)

    def on_front(self):
        if len(self.__elements) > 0:
            return self.__elements[0]
        else:
            return None

    def move_to_end(self):
        element = self.atention()

        if element is not None:
            self.arrive(element)


cola_1 = Queue()
cola_2 = Queue()


# Barrido de la Queue (Imprime todos los valores dentro de esta)

for i in range(cola_1.size()):
    print(cola_1.on_front())

    cola_1.move_to_end()



