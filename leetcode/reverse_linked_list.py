from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    new_list = None

    while head:
        next_node = head.next
        head.next = new_list
        new_list = head
        head = next_node

    return new_list



# # Test case 1
# head = [1,2,3,4,5]
# print(reverseList(head)) # Output [5,4,3,2,1]

# # Test case 2
# head = [1,2]
# print(reverseList(head)) # Output [2,1]

# Test case 3
head = []
print(reverseList(head)) # Output []