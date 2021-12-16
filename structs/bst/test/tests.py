import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))

import unittest
from bst import (
    Node, insert, find, find_min, delete, inorder, inorder_2, inorder_iterative, preorder, preorder_2, dfs,
    postorder, postorder_2, postorder_iterative, bfs, level_order, mirror, is_same, size, 
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
    
    def test_inorder_2(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
        
        self.assertEqual(inorder_2(root), [1, 3, 4, 5, 6, 7, 10, 100, 200])

    def test_inorder_iterative(self):
        root = Node(10)
        insert(root, 5)
        insert(root, 15)
        insert(root, 1)
        insert(root, 6)
        insert(root, 11)
        insert(root, 16)

        self.assertEqual(inorder_iterative(root), [1, 5, 6, 10, 11, 15, 16])
        self.assertEqual(inorder_iterative(root), [1, 5, 6, 10, 11, 15, 16])

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

    def test_preorder_2(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
        
        self.assertEqual(preorder_2(root), [4, 1, 3, 6, 5, 7, 10, 100, 200])


    def test_preorder_iterative(self):
        root = Node(10)
        insert(root, 5)
        insert(root, 15)
        insert(root, 1)
        insert(root, 6)
        insert(root, 11)
        insert(root, 16)

        self.assertEqual(dfs(root), [10, 5, 1, 6, 15, 11, 16])

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
    
    def test_postorder_2(self):
        root = Node(4)
        insert(root, 1)
        insert(root, 3)
        insert(root, 6)
        insert(root, 7)
        insert(root, 5)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)
        
        self.assertEqual(postorder_2(root), [3, 1, 5, 200, 100, 10, 7, 6, 4])

    def test_postorder_iterative(self):
        root = Node(10)
        insert(root, 5)
        insert(root, 15)
        insert(root, 1)
        insert(root, 6)
        insert(root, 11)
        insert(root, 16)

        self.assertEqual(postorder_iterative(root), [1, 6, 5, 11, 16, 15, 10])
       
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
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        current_path_sum = []
        all_paths_sum = []
        expected = root_to_leaf_path_sum(root, current_path_sum, all_paths_sum)
        self.assertEqual(expected, [9, 18, 322]) == expected
    
    def test_hasPathSum(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(hasPathSum(root, 9), True)
        self.assertTrue(hasPathSum(root, 9))
        self.assertEqual(hasPathSum(root, 40), False)
        self.assertFalse(hasPathSum(root, 40))
        self.assertEqual(hasPathSum(root, 322), True)
        self.assertTrue(hasPathSum(root, 322))

    def test_sumOfLeftLeaves(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(sumOfLeftLeaves(root), 7)

    def test_insert_duplicate_node(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        insert_duplicate_node(root)
        expected = bfs(root)
        self.assertEqual(expected, [5, 5, 7, 1, 7, 10, 1, 3, 6, 10, 100, 3, 6, 100, 200, 200])

    def test_getLevel(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertEqual(getLevel(root, 400), 0)
        self.assertEqual(getLevel(root, 10), 3)
        self.assertEqual(getLevel(root, 5), 1)

    def test_nodes_by_level(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        pass
    
    def test_is_bst(self):
        pass

    def test_isSymmetric(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        self.assertFalse(isSymmetric(root))

    def test_invertTree(self):
        root = Node(5)
        insert(root, 1)
        insert(root, 3)
        insert(root, 7)
        insert(root, 6)
        insert(root, 10)
        insert(root, 100)
        insert(root, 200)

        invertTree(root)
        expected_backorder = []
        inorder(root, expected_backorder)
        self.assertEqual(expected_backorder, [200, 100, 10, 7, 6, 5, 3, 1]) 

    def test_isSubtree(self):
        root = Node(50)
        insert(root, 40)
        insert(root, 30)
        insert(root, 45)
        insert(root, 55)
        subRoot = Node(40)
        insert(subRoot, 30)
        insert(subRoot, 45)
        
        expected = isSubtree(root, subRoot) 
        self.assertTrue(expected)

        subRoot2 = Node(40)
        insert(subRoot2, 28)
        insert(subRoot2, 43)

        expected2 = isSubtree(root, subRoot2) 
        self.assertFalse(expected2)

if __name__ == '__main__':
    unittest.main()
