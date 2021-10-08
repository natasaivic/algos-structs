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
        pass

    def test_inorder(self):
        pass

    def test_preorder(self):
        pass

    def test_postorder(self):
        pass
    
    def test_bfs(self):
        pass

    def test_level_order(self):
        pass

    def test_dfs(self):
        pass

    def test_mirror(self):
        pass

    def test_is_same(self):
        pass

    def test_size(self):
        pass

    def test_size_2(self):
        pass

    def test_size_3(self):
        pass
    
    def test_size_4(self):
        pass

    def test_find_tree_height(self):
        pass

    def test_min_value(self):
        pass

    def test_max_value(self):
        pass

    def test_find_max_path(self):
        pass

    def test_find_min_path(self):
        pass

    def test_root_to_leaf_path(self):
        pass

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
