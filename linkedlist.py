class Node:
    def __init__(self, data):
            self.data=data 
            self.next=next

class Linkedlist:
    def __init__(self):
        
            self.head=None

    

    def insert(self , data):
        new_node =Node(data)

        
    def insert_at_beginning(self, data):
            
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

