from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Attach remaining nodes
        tail.next = list1 if list1 else list2

        return dummy.next

    def mid(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head.next  # Start fast at head.next for correct split

        while fast and fast.next:  # Fix to prevent NoneType errors
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:  # Fix base condition
            return head

        left = head
        mid_node = self.mid(head)  # Get mid node
        right = mid_node.next
        mid_node.next = None  # Split list into two halves

        left = self.sortList(left)  # Recursively sort left half
        right = self.sortList(right)  # Recursively sort right half

        return self.merge(left, right)   
