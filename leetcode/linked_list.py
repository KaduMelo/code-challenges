class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if (current):
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def insert(self, new_element, position):
        count=1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
        pass

    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current.next
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def print(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

# Test cases
# Set up some Elements
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)

# Start setting up a LinkedList
ll = LinkedList(e1)


ll.append(e2)
ll.append(e3)

print(ll.print())

# Test get_position
# Should print 3
print("print 3",ll.head.next.next.value)

# Test insert
ll.insert(e4,3)

#Test delete
ll.delete(1)
print(ll.print())