import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

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

        self.assertEqual(my_stack.__repr__(), "1 -> 0 -> 0 -> 8 -> 8 -> 6 -> None")

    def test_pop(self):
        my_stack = Stack()
        my_stack.push(6)
        my_stack.push(8)
        my_stack.push(8)
        my_stack.push(0)
        my_stack.push(0)
        my_stack.push(1)

        self.assertEqual(my_stack.pop(), 1)

if __name__ == '__main__':
    unittest.main()