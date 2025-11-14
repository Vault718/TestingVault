class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_head(data)
            return
        
        new_node = Node(data)
        cur = self.head
        idx = 0
        
        while cur and idx < position - 1:
            cur = cur.next
            idx += 1
        
        if not cur:
            raise IndexError("Position out of bounds")

        new_node.next = cur.next
        cur.next = new_node

    def delete_value(self, value):
        if not self.head:
            return
        
        if self.head.data == value:
            self.head = self.head.next
            return
        
        cur = self.head
        while cur.next and cur.next.data != value:
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next

    def search(self, value):
        cur = self.head
        while cur:
            if cur.data == value:
                return True
            cur = cur.next
        return False
