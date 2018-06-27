#O(n)
import unittest

# Tree node
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
depth=0
alldepths = []
def minDepth(root):
    # Corner Case.Should never be hit unless the code is
    # called on root = NULL
    global depth
    global alldepths
    if(len(alldepths)>2):
        return
    if root is None:
        depth=0
        return

    # Base Case : Leaf node.This acoounts for height = 1
    if root.left is None and root.right is None:
        if depth not in alldepths:
            alldepths.append(depth)
        return

    # If left subtree is Null, recur for right subtree
    if root.left is None:
        depth += 1
        minDepth(root.right)
        depth -= 1
        return

    # If right subtree is Null , recur for left subtree
    if root.right is None:
        depth += 1
        minDepth(root.left)
        depth -= 1
        return
    if root.left and root.right:
        depth += 1
        minDepth(root.left)
        minDepth(root.right)
        depth -= 1
        return
    return






def is_balanced(tree_root):
    # Determine if the tree is superbalanced
    minDepth(tree_root)
    global alldepths
    global depth
    if (len(alldepths) == 2):
        x = abs(alldepths[0]-alldepths[1])
        if x == 1:
            alldepths = []
            depth = 0
            return True
    if (len(alldepths)<=1):
        alldepths = []
        depth = 0
        return True
    alldepths=[]
    depth=0
    return False



# Tests

class Test(unittest.TestCase):

    class BinaryTreeNode(object):

        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def insert_left(self, value):
            self.left = Test.BinaryTreeNode(value)
            return self.left

        def insert_right(self, value):
            self.right = Test.BinaryTreeNode(value)
            return self.right

    def test_full_tree(self):
        tree = Test.BinaryTreeNode(5)
        left = tree.insert_left(8)
        right = tree.insert_right(6)
        left.insert_left(1)
        left.insert_right(2)
        right.insert_left(3)
        right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_leaves_at_the_same_depth(self):
        tree = Test.BinaryTreeNode(3)
        left = tree.insert_left(4)
        right = tree.insert_right(2)
        left.insert_left(1)
        right.insert_right(9)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_one(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right.insert_right(7)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_leaf_heights_differ_by_two(self):
        tree = Test.BinaryTreeNode(6)
        left = tree.insert_left(1)
        right = tree.insert_right(0)
        right_right = right.insert_right(7)
        right_right.insert_right(8)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_three_leaves_total(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right.insert_left(8)
        right.insert_right(5)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_both_subtrees_superbalanced(self):
        tree = Test.BinaryTreeNode(1)
        left = tree.insert_left(5)
        right = tree.insert_right(9)
        right_left = right.insert_left(8)
        right.insert_right(5)
        right_left.insert_left(7)
        result = is_balanced(tree)
        self.assertFalse(result)

    def test_only_one_node(self):
        tree = Test.BinaryTreeNode(1)
        result = is_balanced(tree)
        self.assertTrue(result)

    def test_linked_list_tree(self):
        tree = Test.BinaryTreeNode(1)
        right = tree.insert_left(2)
        right_right = right.insert_right(3)
        right_right.insert_right(4)
        result = is_balanced(tree)
        self.assertTrue(result)


unittest.main(verbosity=2)