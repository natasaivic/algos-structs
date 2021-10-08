import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

import unittest
from list import List


class ListTest(unittest.TestCase):
    def test_append(self):
        list = List()
        list.append(1)
        list.append(2)
        list.append(3)

        self.assertEqual(list.__repr__(), "1 -> 2 -> 3 -> None")

    def test_find(self):
        list = List()
        list.append(1)
        list.append(2)
        list.append(3)

        self.assertTrue(list.find(1))

    def test_delete(self):
        list = List()
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.append(5)
        list.delete(5)

        self.assertEqual(list.__repr__(), "1 -> 2 -> 3 -> 4 -> None")

        list.append(6)
        list.append(7)
        list.append(10)
        list.delete(10)

        self.assertEqual(list.__repr__(), "1 -> 2 -> 3 -> 4 -> 6 -> 7 -> None")

    def test_prepend(self):
        list = List()
        list.append(1)
        list.append(2)
        list.append(3)
        list.append(4)
        list.prepend(0)

        self.assertEqual(list.__repr__(), "0 -> 1 -> 2 -> 3 -> 4 -> None")

    def test_find_nth(self):
        list = List()
        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)
        list.append(1)

        self.assertEqual(list.find_nth(4), 0)

    def test_find_nth_last(self):
        list = List()
        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)
        list.append(1)

        self.assertEqual(list.find_nth_last(1), 1)
        self.assertEqual(list.find_nth_last(2), 0)

    def test_removeNthFromEnd(self):
        list = List()
        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)
        list.append(1)
        list.removeNthFromEnd(1)

        self.assertEqual(list.__repr__(), "2 -> 5 -> 8 -> 0 -> 0 -> None")

    def test_find_middle(self):
        list = List()
        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)

        self.assertEqual(list.find_middle(), 8)

    def test_replace(self):
        list = List()
        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)
        list.append(1)
        list.replace(2, 6)

        self.assertEqual(list.__repr__(), "6 -> 5 -> 8 -> 0 -> 0 -> 1 -> None")

        list.replace(5, 6)

        self.assertEqual(list.__repr__(), "6 -> 6 -> 8 -> 0 -> 0 -> 1 -> None")

    def test_suma(self):
        list = List()
        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)
        list.append(1)

        self.assertEqual(list.suma(), 16)

    def test_is_empty(self):
        list = List()

        self.assertTrue(list.is_empty())

        list.append(2)
        list.append(5)
        list.append(8)
        list.append(0)
        list.append(0)
        list.append(1)

        self.assertFalse(list.is_empty())


if __name__ == '__main__':
    unittest.main()
