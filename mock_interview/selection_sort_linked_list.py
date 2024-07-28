class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self, head = None) -> None:
        self.head = head 

    def remove_node (self, node_to_be_removed) -> Node:

        if node_to_be_removed == self.head:

            next_node = node_to_be_removed.next
            self.head = next_node
            node_to_be_removed.next = None

        else:
            curr_node = self.head

            while curr_node.next != node_to_be_removed:
                curr_node = curr_node.next

            prev_node = curr_node
            next_node = curr_node.next.next 

            prev_node.next = next_node
            node_to_be_removed.next = None

    def append (self, node_to_add):

        if not self.head:
            self.head = node_to_add

        else:
            curr_node = self.head 

            while curr_node.next:
                curr_node = curr_node.next

            curr_node.next = node_to_add

    def print_linked_list (self) -> None:
        curr_node = self.head

        while curr_node:
            print ( curr_node.val )
            curr_node = curr_node.next

    def min ( self ) -> Node:

        curr_node = self.head
        min_val_node = curr_node

        while curr_node:

            if curr_node.val < min_val_node.val:
                min_val_node = curr_node
            
            curr_node = curr_node.next

        return min_val_node

def selection_sort (ll : LinkedList):
    sorted_ll = LinkedList()

    while ll.head:
        sorted_ll.append (ll.remove_node(ll.min()))

    return sorted_ll

head = Node(5)
ll = LinkedList(head)

list_of_node_vals = [3, 2, 8, 4]

for node_val in list_of_node_vals:
    new_node = Node(node_val)
    ll.append(new_node)

sorted_ll = selection_sort ( ll )
sorted_ll.print_linked_list()