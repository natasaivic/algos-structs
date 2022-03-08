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

    def prepend(self, value):
        temp_node = Node(value)
        temp_node.next = self.head
        self.head = temp_node
        return self.head

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
        current = self.get_head()
        while current.next is not None:
            current = current.next
        current.next = new_node
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
            return
        current = self.head
        while current.next is not None:
            print(current.value, end=" -> ")
            current = current.next
        print(current.value, "-> None")
        return

    def delete_at_head(self):
        first_element = self.get_head()
        # If List is not empty then link head to the
        # nextElement of firstElement.
        if first_element is not None:
            self.head = first_element.next
            first_element.next = None
        return

    def delete(self, value):
        deleted = False
        if self.is_empty():  
            print("List is Empty")
            return deleted

        if self.get_head().value == value:
            self.head = self.head.next
            deleted = True
            return deleted

        previous = self.get_head()
        current = self.get_head().next
        while current is not None:
            if current.value == value:
                previous.next = current.next
                deleted = True
                break
            previous = current
            current = current.next

        return deleted

    def search(self, search_value):
        if self.is_empty():
            print("List is Empty")
            return None
        current = self.head
        while current is not None:
            if current.value == search_value:
                return current
            current = current.next

        print(search_value, " is not in List!")
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
