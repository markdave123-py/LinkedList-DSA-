class SinglyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None


L1 = SinglyLinkedList(1)
L2 = SinglyLinkedList(2)
L3 = SinglyLinkedList(3)

L1.next = L2
L2.next = L3



class DoublyLinkedList(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prevNode = None

L1 = DoublyLinkedList(1)
L2 = DoublyLinkedList(2)
L3 = DoublyLinkedList(3)

L1.next = L2
L2.prevNode = L1
L2.next = L3
L3.prevNode = L2


def check_cycle(node):
    pointer1 = node
    pointer2 = node 

    while pointer2 != None and pointer2.next != None:
        pointer1 = node.next
        pointer2 = node.next.next

        if pointer1 == pointer2:
            return True 


    return False


def reverse(head):
    current = head 
    previous = None
    nextNode = None

    while current:
        nextNode = current.next 
        current.next = previous

        previous = current

        current = nextNode


    return previous


