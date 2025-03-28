class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.__top = None  # Referencia al nodo superior de la pila

    def push(self, dato):
        # Agrega un elemento a la pila
        new_node = Node(dato)
        new_node.next = self.__top
        self.__top = new_node

    def pop(self):
        # Devuelve y luego elimina el último elemento de la pila
        if self.__top is None:
            return None
        last_data = self.__top.data
        self.__top = self.__top.next
        return last_data

# Ejemplo
stack = Stack()
stack.push(1)
stack.push(20)
stack.push(0)
stack.push(4)
stack.push(5)

# Salida esperada
print(stack.pop())  # 5
print(stack.pop())  # 4
print(stack.pop())  # 0
print(stack.pop())  # 2
print(stack.pop())  # 1
print(stack.pop())  # None


