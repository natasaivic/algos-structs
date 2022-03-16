class Node:
    def __init__(self, data):
        self.data = data  # Data field
        self.next_element = None  # Pointer to next node


# get_head() - returns the head of the list
# insert_at_tail(data) - inserts an element at the end of the linked list
# insert_at_head(data) - inserts an element at the start/head of the linked list
# delete(data) - deletes an element with your specified value from the linked list
# delete_at_head() - deletes the first element of the list
# search(data) - searches for an element with the specified value in the linked list
# is_empty() - returns true if the linked list is empty

class LinkedList:
    def __init__(self):
        self.head_node = None  # Pointer to first node

    def get_head(self):
        return self.head_node

    def is_empty(self):
        if self.head_node is None:  # Check whether the head is None
            return True
        else:
            return False


lst = LinkedList()  # Linked List created
print(lst.is_empty())  # Returns true


