class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def add_node_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_node_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def delete_node_at_beginning(self):
        if not self.head:
            print("Nothing to delete")
            return
        self.head = self.head.next

    def delete_node_at_end(self):
        if not self.head:
            print("Nothing to delete")
            return
        if not self.head.next:
            self.head = None
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None
        
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" --> ")
            current_node = current_node.next   
        print("None")  # To signify the end of the list


if __name__ == "__main__":
    ll = LinkedList()
    ll.delete_node_at_beginning()  # Expected: Nothing to delete
    ll.add_node_at_beginning(1)
    ll.print_list()  # Expected: 1 --> None
    ll.add_node_at_beginning(3)
    ll.print_list()  # Expected: 3 --> 1 --> None
    ll.add_node_at_end(5)
    ll.print_list()  # Expected: 3 --> 1 --> 5 --> None
    ll.delete_node_at_beginning()
    ll.print_list()  # Expected: 1 --> 5 --> None
    ll.add_node_at_beginning("stringtest")
    ll.print_list()  # Expected: stringtest --> 1 --> 5 --> None
    ll.delete_node_at_end()
    ll.print_list()  # Expected: stringtest --> 1 --> None

