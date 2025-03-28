class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None


    #metodo para ingresar a la fila (ultimo dato ingresado) (dato en la parte de atrás de la fila)
    def enqueue(self, item):
        new_node = Node(item)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    #metodo para salir de la fila (primer dato ingresado) (dato al frente de la fila)
    def dequeue(self):
        if not self.front:
            return None
        value = self.front.value
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return value

#crear instancia de la clase Queue
queue = Queue()
#usar la instacia para acceder a los metodos de la clase
#insertar datos 
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(48)
queue.enqueue(5)

#imprimir datos
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
#print(queue.dequeue())
print(queue.dequeue())
#print(queue.dequeue())
