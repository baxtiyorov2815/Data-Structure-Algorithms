# Linked List
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.size = 0 if head is None else 1
    
    def appendToEnd(self, val):
        newNode = Node(val=val)
        if not self.head:
            self.head = newNode
            return
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = newNode
        self.size += 1
    
    def appendToHead(self, val):
    
        newNode = Node(val=val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
    
    def insert(self, index, val):
        newNode = Node(val=val)
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.appendToHead(val)
            return
        
        if index == self.size:
            self.appendToEnd(val)
            return

        newNode = Node(val=val)
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        newNode.next = current.next
        current.next = newNode
        self.size += 1
    
    def getByIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        i = 0
        current = self.head
        while current:
            if i == index:
                return current.val
            current = current.next
            i += 1
        
        raise IndexError
    
    def getIndex(self, val):
        i = 0
        current = self.head
        while current:
            if current.val == val:
                return i
            
            current = current.next
            i += 1
        
        return -1

    def check(self, index, val):
        try:
            return self.getByIndex(index) == val
        except:
            return False
    
    def deleteByIndex(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        
        self.size -= 1
    
    def deleteByValue(self, val):
        if self.size == 1 and self.head.val == val:
            self.head = None
            self.size = 0
            return 

        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
            
            current = current.next
        
    def __len__(self):
        return self.size

    def __str__(self):
        res = ""
        current = self.head
        while current:
            res += f"{current.val} -> "
            current = current.next
        res += "None"
        return res