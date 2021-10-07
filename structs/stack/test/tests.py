import sys
sys.path.insert(0, '..')

import unittest
from stack import Stack


class StackTest(unittest.TestCase):
    def test_push(self):
        my_stack = Stack()
        my_stack.push(6)
        my_stack.push(8)
        my_stack.push(8)
        my_stack.push(0)
        my_stack.push(0)
        my_stack.push(1)

        self.assertEqual(my_stack.__repr__(), "6 -> 6 -> 8 -> 0 -> 0 -> 1 -> None")

    def test_pop(self):
        my_stack = Stack()
        my_stack.push(6)
        my_stack.push(8)
        my_stack.push(8)
        my_stack.push(0)
        my_stack.push(0)
        my_stack.push(1)

        self.assertEqual(my_stack.deque(), 6)

if __name__ == '__main__':
    unittest.main()