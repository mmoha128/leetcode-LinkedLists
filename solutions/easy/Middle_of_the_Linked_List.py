from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def lengthll(self):
        cur = self.head
        total = 0
        while cur!=None:
            total +=1
            cur = cur.next
        return total

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head,head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow 
