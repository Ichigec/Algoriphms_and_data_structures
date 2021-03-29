class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        node = self.head
        from_linked_list=[]
        while node is not None:
            if node.value == val:
                from_linked_list.append(node.value)
            node=node.next
        return from_linked_list # здесь будет ваш код

    def delete(self, val, all=False):
        #node = self.find(val)
        #node.
        if all!=False:
            current=self.head
            while current is not None:
                if current.value==val:
                    previous.next=current.next
                    current=None
                    current=previous
                previous=current
                current=current.next
            if current ==None:
                return
            
        else:
            current=self.head
            if current is not None:
                if current.value==val:
                    self.head=current.next
                    current=None
                    return
            while current is not None:
                if current.value==val:
                    break
                previous=current
                current=current.next
            if current ==None:
                return
            previous.next=current.next
            current=None
            
        
        #pass # здесь будет ваш код'''

    def clean(self):
        self.__init__()
        
        #pass # здесь будет ваш код

    def len(self):
        x=0
        node = self.head
        while node is not None:
            x+1
            node=node.next
        return x # здесь будет ваш код

    def insert(self, afterNode, newNode):
        current = self.head
        previous = None
        valueToFind=afterNode
        while current.value != valueToFind: 
            previous = current 
            current = current.next
        if current.value == valueToFind:
            previous = current 
            current = current.next

            previous.next = newNode 
            previous = previous.next 
            previous.next = current
        #pass # здесь будет ваш код