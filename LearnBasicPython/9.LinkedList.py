
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


    def ReverseLinkedList(self):
        print("Starting to reverse the linked list")
        current, previous = self.head, None
        
        while current:
            print(f"Current Node: {current.data}, Previous Node: {previous.data if previous else None}")
            
            temp = current.next  # Save the next node
            print(f"Next node saved: {temp.data if temp else None}")
            
            current.next = previous  # Reverse the link
            print(f"Reversing link: {current.data} now points to {previous.data if previous else None}")
            
            previous = current  # Move previous to current node
            current = temp  # Move to the next node in the original list
            
            print(f"Moved to next node: Current is {current.data if current else None}, Previous is {previous.data}")

        self.head = previous  # Update head to the new front of the list
        print("Linked list reversal complete")


    #Take a missdle of linkedlist
    def FindMiddleOfLinkedList(self):
        print("Middle of  LinkedList")
        slow , fast = head ,head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        

if __name__ == "__main__":
    ll = LinkedList()
    ll.delete_node_at_beginning()  # Expected: Nothing to delete
    ll.add_node_at_beginning(5)
    ll.print_list()  # Expected: 1 --> None
    ll.add_node_at_beginning(3)
    ll.print_list()  # Expected: 3 --> 1 --> None
    ll.add_node_at_end(1)
    ll.print_list()  # Expected: 3 --> 1 --> 5 --> None
    #ll.delete_node_at_beginning()
    ll.print_list()  # Expected: 1 --> 5 --> None
    ll.add_node_at_beginning("8")
    ll.print_list()  # Expected: stringtest --> 1 --> 5 --> None
    #`ll.delete_node_at_end()
    ll.print_list()  # Expected: stringtest --> 1 --> None
    ll.ReverseLinkedList()
    ll.print_list()
    ll.FindMiddleOfLinkedList()
    ll.print_list() 


