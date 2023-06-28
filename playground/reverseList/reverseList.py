# reverse a linked list

class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None

  def reverse(self):
    prev = None
    current = self.head
    while current != None:
      next = current.next
      current.next = prev
      prev = current
      current = next
    self.head = prev
    
# how to test this

if __name__ == "__main__":
  llist = LinkedList()
  llist.head = Node(1)
  second = Node(2)
  third = Node(3)
  llist.head.next = second
  second.next = third
  llist.reverse()
  print(llist.head.val)
  print(llist.head.next.val)
  print(llist.head.next.next.val)
  print(llist.head.next.next.next)