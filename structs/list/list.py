class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"{self.value} -> {self.next}"

class List:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = node
        
    def prepend(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    # insert node in sorted list
    def insert(self, node):
        if self.head is None:
            return None

        prev = None
        current = self.head
        while current is not None:
            if current.value > node.value:
                if prev is not None:
                    prev.next = node
                    node.next = current
                    return self.head
                else:
                    node.next = self.head
                    self.head = node
                    return self.head
            prev = current
            current = current.next
        prev.next = node
        return self.head

    # insert value on k-th place of an unsorted list if k <= n, else append
    def insert_node_on_kth(self, k, node):
        if self.head is None:
            return None

        if k == 0 or k == 1:
            node.next = self.head
            self.head = node
            return self.head

        prev = None
        current = self.head
        for i in range(1, k):
            if current is None:
                prev.next = node
                return self.head
            prev = current
            current = current.next
        prev.next = node
        node.next = current

        return self.head

    def find(self, search_value):
        if self.head is None:
            return False

        current = self.head
        while current is not None:
            if current.value == search_value:
                return True
            current = current.next
        return False
    
    def find_nth(self, n):
        if self.head is None:
            return None
            
        current = self.head
        for i in range(1, n):
            if current is None:
                return None
            current = current.next
        return current.value
    
    def find_nth_last(self, n):
        if self.head is None:
            return None
        
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        
        if length < n:
            return None

        current = self.head
        for i in range(0, length - n):
            current = current.next
        return current.value

    def count(self):
        if self.head is None:
            return 0
        
        length = 0
        current = self.head
        while current is not None:
            length += 1
            current = current.next
        return length

    def removeNthFromEnd(self, n):
        slow = self.head
        fast = self.head

        for i in range(n):
            fast = fast.next
        
        if fast is None:
            return self.head.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next

        return self.head

    def find_middle(self):
        if self.head is None:
            return None
        
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def delete_middle(self):
        if self.head is None:
            return
        if self.head.next is None:
            return None
        
        temp = self.head
        slow, fast = self.head, self.head
        while fast and fast.next:
            temp = slow
            slow = slow.next
            fast = fast.next.next
        
        temp.next = slow.next
        return self.head

    # unsorted list
    # unique elements
    def delete(self, value):
        if self.head is None:
            return False
        
        if self.head.value == value:
            self.head = self.head.next
            return True
        
        previous = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                previous.next = current.next
                return True
            previous = current
            current = current.next
        return False
    
    # unsorted list
    # unique elements
    def delete2(self, value):
        if self.head is None:
            return None
        
        if self.head.value == value:
            self.head = self.head.next
            return self.head

        previous = self.head
        current = self.head.next
        while current is not None:
            if current.value == value:
                previous.next = current.next
                return self.head
            previous = current
            current = current.next
        return f"Non existing number."

    # unsorted list
    # with duplicates 
    # Given an integer value, remove all the nodes of the linked list that has Node.value == n, and return the new head.
    # 1 -> 1 -> 1 -> 2 -> 3 -> 1 -> 4 -> None  
    # remove_elements(1)
    # output: 2 -> 3 -> 4 -> None
    def remove_elements(self, value): 
        if self.head is None:
            return None

        while self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                return None
        
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                continue
            current = current.next
        
        return self.head
    
    # sorted list
    # with duplicates
    def remove_duplicates_2(self, value):
        if self.head is None:
            return None
    
        while self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                return None

        done = False
        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                done = True
                continue
            else:
                if done is False:
                    current = current.next
                else:
                    break
        return self.head

    # sorted
    # Remove all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.
    def remove_all_duplicates_and_its_orginals(self):
        if self.head is None:
            return None

        dummy_node = List()
        dummy_node.next = self.head
        previous = dummy_node
        current = self.head

        while current and current.next:
            if current.value == current.next.value:
                node = current
                while node and node.value == current.value:
                    node = node.next
                current = node
                previous.next = node
            else:
                previous = current
                current = current.next
        return dummy_node.next

    # Remove all duplicates such that each element appears only once. Return the linked list sorted as well.
    def remove_duplicates_from_sorted_list(self): # 1 -> 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> None
        if self.head is None:
            return None
        
        current = self.head
        while current.next is not None:
            if current.value == current.next.value:
                current = current.next.next
            else:
                current = current.next
        return self.head

    def is_empty(self):
        return self.head is None
    
    def replace(self, n, m):
        if self.head is None:
            return False
        
        current = self.head
        while current is not None:
            if current.value == n:
                current.value = m
                return True
            current = current.next
        return False

    def replace_all_duplicates(self, n, m):
        if self.head is None:
            return None
        
        current = self.head
        while current is not None:
            if current.value == n:
                current.value = m
            current = current.next
        return self.head

    def suma(self):
        suma = 0
        current = self.head
        while current is not None:
            suma += current.value
            current = current.next
        return suma

    def is_cyclic(self, head):
        slow = self.head
        fast = self.head

        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                print(f"{fast} -> {slow}")
                return True
        return False

    def reverse(self):
        if self.head is None:
            return None

        previous = None
        while self.head is not None:
            temp = self.head.next
            self.head.next = previous
            previous = self.head
            self.head = temp
        return previous

    def reverse_between(self, left, right):
        if self.head is None:
            return None
        
        previous = None
        current = self.head
        while left > 1:
            previous = current
            current = current.next
            left -= 1
            right -= 1

        connection = previous
        tail = current
        while right > 0:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            right -= 1

        if connection is not None:
            connection.next = previous
        else:
            self.head = previous
        
        tail.next = current
        return self.head

    def odd_even(self):
        if self.head is None:
            return None
        
        odd = self.head
        even = self.head.next
        evenHead = even
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenHead
        return self.head

    def is_palindrome(self):
        if self.head is None:
            return

        # 1st step: Locate the mid point of linked list
        # [1 2 3]
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            fast = fast.next.next  
            if fast is not None:
                slow = slow.next
        mid = slow #head of the second half
    
        # 2nd step: Reverse second half of linked list
        prev = None
        current = mid 
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        head_2 = prev

        current = self.head
        while current is not None and head_2 is not None:
            if current.value != head_2.value:
                return False
            current = current.next
            head_2 = head_2.next
        return True

    def swap_nodes_in_pairs(self):
        temp = Node(0)
        temp.next = self.head
        current = temp

        while current.next is not None and current.next.next is not None:
            first_node = current.next
            second_node = current.next.next
            first_node.next = second_node.next
            current.next = second_node
            current.next.next = first_node
            current = current.next.next
        return temp.next

    def rotate_right_by_k_places(self, k):
        right = self.head
        left = self.head
        for i in range(1, k):
            left = left.next

        # Find kth node from right
        # by finding tail node
        tail = left
        while tail.next.next is not None:
            right = right.next 
            tail = tail.next
        tail = tail.next

        new_head = right.next
        right.next = None
        tail.next = self.head

        return new_head

    def __repr__(self):
        return f"{self.head}"
        