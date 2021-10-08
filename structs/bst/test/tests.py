import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

import unittest
from bst import (
    Node, insert, find, delete, inorder, preorder, 
    postorder, bfs, level_order, dfs, mirror, is_same, size, 
    size_2, size_3, size_4, find_tree_height, min_value, 
    max_value, find_max_path, find_min_path, root_to_leaf_path, 
    root_to_leaf_path_sum, hasPathSum, sumOfLeftLeaves, insert_duplicate_node, 
    getLevel, nodes_by_level, isSymmetric, invertTree, is_same_tree, isSubtree
)


class BstTest(unittest.TestCase):
    def test_append(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 2)
        insert(root, 3)
        insert(root, 6)
        insert(root, 9)
        insert(root, 7)
        insert(root, 5)
        insert(root, 8)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
    
    def test_find(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 2)
        insert(root, 3)
        insert(root, 6)
        insert(root, 9)
        insert(root, 7)
        insert(root, 5)
        insert(root, 8)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertTrue(find(root, 1))
        self.assertTrue(find(root, 8))
        self.assertTrue(find(root, 100))
        self.assertFalse(find(root, 13))

    def test_delete(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 2)
        insert(root, 3)
        insert(root, 6)
        insert(root, 9)
        insert(root, 7)
        insert(root, 5)
        insert(root, 8)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
        delete(root, 10)
        delete(root, 100)

        self.assertFalse(find(root, 10))
        self.assertFalse(find(root, 100))

    def test_inorder(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        lista_inorder = []
        inorder(root, lista_inorder)
        self.assertEqual(lista_inorder, [1, 3, 4, 5, 6, 7, 10, 100, 200])

    def test_preorder(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
        
        lista_preorder = []
        preorder(root, lista_preorder)
        self.assertEqual(lista_preorder, [4, 1, 3, 6, 5, 7, 10, 100, 200])

    def test_postorder(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
        
        lista_postorder = []
        postorder(root, lista_postorder)
        self.assertEqual(lista_postorder, [3, 1, 5, 200, 100, 10, 7, 6, 4])
    
    # Level order using queue data structure
    def test_bfs(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(bfs(root), [4, 1, 6, 3, 5, 7, 10, 100, 200])
        
    def test_level_order(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(level_order(root), [[4], [1, 6], [3, 5, 7], [10], [100], [200]])

    def test_dfs(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(dfs(root), [4, 1, 3, 6, 5, 7, 10, 100, 200])

    def test_mirror(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        lista_inorder = []
        inorder(root, lista_inorder)
        lista_inorder.reverse() 

        mirror(root)
        lista_inorder_mirror = []
        inorder(root, lista_inorder_mirror)

        self.assertEqual(lista_inorder, lista_inorder_mirror)

    def test_is_same(self):
        root1 = Node(4)
        insert(root1, 1)
        insert(root1, 2)
        insert(root1, 3)
        insert(root1, 6)

        root2 = Node(4)
        insert(root2, 1)
        insert(root2, 2)
        insert(root2, 3)
        insert(root2, 6)

        root3 = Node(4)
        insert(root3, 1)
        insert(root3, 2)
        insert(root3, 9) 
        insert(root3, 6)

        self.assertEqual(is_same(root1, root2), True)
        self.assertTrue(is_same(root1, root2))
        self.assertEqual(is_same(root1, root3), False)
        self.assertFalse(is_same(root1, root3))
        self.assertEqual(is_same(root2, root3), False)
        self.assertFalse(is_same(root2, root3))

    def test_size(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(size(root), 9)

    def test_size_2(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(size_2(root), 9)

    def test_size_3(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(size_3(root), 9)
    
    def test_size_4(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(size_4(root), 2)

    def test_find_tree_height(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(find_tree_height(root), 6)

    def test_min_value(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(min_value(root), 1)

    def test_max_value(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(max_value(root), 200)

    def test_find_max_path(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(find_max_path(root), 327)

    def test_find_min_path(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(find_min_path(root), 5)

    def test_root_to_leaf_path(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        current_path = []
        all_paths = []
        expected = root_to_leaf_path(root, current_path, all_paths)
        self.assertEqual(expected, [[5, 1, 3], [5, 7, 6], [5, 7, 10, 100, 200]])

    def test_root_to_leaf_path_sum(self):
        pass
    
    def test_hasPathSum(self):
        pass

    def test_sumOfLeftLeaves(self):
        pass

    def test_insert_duplicate_node(self):
        pass

    def test_getLevel(self):
        pass

    def test_nodes_by_level(self):
        pass

    def test_isSymmetric(self):
        pass

    def test_invertTree(self):
        pass

    def test_is_same_tree(self):
        pass

    def test_isSubtree(self):
        pass


if __name__ == '__main__':
    unittest.main()
