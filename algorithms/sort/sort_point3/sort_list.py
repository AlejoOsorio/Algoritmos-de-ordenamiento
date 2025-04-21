# Python Program to sort a linked list of 0s, 1s or 2s

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None

# Function to sort a linked list of 0s, 1s and 2s
def sort_list(head):

    # O(1): inicialización del contador
    cnt = [0, 0, 0]
    ptr = head

    # O(n): recorrer la lista enlazada y contar ocurrencias de 0, 1 y 2
    while ptr is not None:
        cnt[ptr.data] += 1
        ptr = ptr.next

    idx = 0
    ptr = head

    # O(n): recorrer nuevamente para reescribir los valores en orden
    while ptr is not None:
        if cnt[idx] == 0:
            idx += 1  # O(1): avanzar al siguiente valor
        else:
            ptr.data = idx  # O(1): asignar nuevo valor
            cnt[idx] -= 1   # O(1): actualizar contador
            ptr = ptr.next  # O(1): avanzar en la lista

# O(n): imprimir la lista enlazada
def print_list(node):
    while node is not None:
        print(f" {node.data}", end='')
        node = node.next
    print("\n")  # O(1)

# --- Ejecución del programa ---
if __name__ == "__main__":

    # O(1): creación manual de una lista enlazada de 5 nodos
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(1)
    head.next.next.next.next = Node(0)

    print("Linked List before Sorting:", end='')
    print_list(head)  # O(n)

    sort_list(head)   # O(n)

    print("Linked List after Sorting:", end='')
    print_list(head)  # O(n)
