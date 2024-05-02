class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def print_linked_list_with_pointers(head):
    current = head
    while current is not None:
        print(f"({current.value})", end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print("None")

def reverse_linked_list(head):
    prev = None
    current = head
    
    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
        
        print("Linked list after this step:")
        print_linked_list_with_pointers(prev)
    
    return prev

# Example usage
# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print("Original linked list:")
print_linked_list_with_pointers(head)

# Reverse the linked list
print("\nReversing the linked list...")
head = reverse_linked_list(head)

print("\nFinal reversed linked list:")
print_linked_list_with_pointers(head)
