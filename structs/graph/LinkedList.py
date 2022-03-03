from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def insert_at_head(self, value):
        temp_node = Node(value)
        if self.is_empty():
            self.head = temp_node
            return self.head

        temp_node.next = self.head
        self.head = temp_node
        return self.head

    def insert_at_tail(self, value):
        new_node = Node(value)
        if self.get_head() is None:
            self.head = new_node
            return
        # if list not empty, traverse the list to the last node
        temp = self.get_head()
        while temp.next is not None:
            temp = temp.next
        # Set the nextElement of the previous node to new node
        temp.next = new_node
        return

    def length(self):
        current = self.get_head()
        length = 0

        # Traverse the list and count the number of nodes
        while current is not None:
            length += 1
            current = current.next
        return length

    def print_list(self):
        if self.is_empty():
            print("List is Empty")
            return False
        temp = self.head
        while temp.next is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print(temp.value, "-> None")
        return True

    def delete_at_head(self):
        # Get Head and firstElement of List
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if first_element is not None:
            self.head = first_element.next
            first_element.next = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():  # Check if list is empty -> Return False
            print("List is Empty")
            return deleted
        current_node = self.get_head()  # Get current node
        previous_node = None  # Get previous node
        if current_node.value == value:
            self.delete_at_head()  # Use the previous function
            deleted = True
            return deleted

        # Traversing/Searching for Node to Delete
        while current_node is not None:
            # Node to delete is found
            if value == current_node.value:
                # previous node now points to next node
                previous_node.next = current_node.next
                current_node.next = None
                deleted = True
                break
            previous_node = current_node
            current_node = current_node.next

        return deleted

    def search(self, value):
        if self.is_empty():
            print("List is Empty")
            return None
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return temp
            temp = temp.next

        print(value, " is not in List!")
        return None

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next:
                    if outer_node.value == inner_node.next.value:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next.next
                        inner_node.next = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next
            outer_node = outer_node.next
        return
