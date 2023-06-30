class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class BinaryTree:
  def pre_order(self, values=[]):
    def walk(input_node, value_list):
      if not input_node:
        return
      value_list.append(input_node.value)
      walk(input_node.left, value_list)
      walk(input_node.right, value_list)
    walk(self.root, values)
    return

  def in_order(self):
    pass

  def post_order(self):
    pass

class BinarySearchTree(BinaryTree):
  def add(self, value):
    pass

  def contains(self, value):
    pass