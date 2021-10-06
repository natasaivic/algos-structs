import sys
sys.path.insert(0, '..')

import unittest
from queue import Queue


class QueueTest(unittest.TestCase):
    def test_enque(self):
        my_queue = Queue()
        my_queue.enque(6)
        my_queue.enque(6)
        my_queue.enque(8)
        my_queue.enque(0)
        my_queue.enque(0)
        my_queue.enque(1)

        self.assertEqual(my_queue.__repr__(), "6 -> 6 -> 8 -> 0 -> 0 -> 1 -> None")

    def test_deque(self):
        my_queue = Queue()
        my_queue.enque(6)
        my_queue.enque(6)
        my_queue.enque(8)
        my_queue.enque(0)
        my_queue.enque(0)
        my_queue.enque(1)

        self.assertEqual(my_queue.deque(), 6)

if __name__ == '__main__':
    unittest.main()