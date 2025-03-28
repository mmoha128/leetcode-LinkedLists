from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)

        lp,cur = dummy, head
        for i in range(left-1):
            lp, cur = cur, cur.next
        
        prev = None
        for i in range(right-left + 1):
            tmpnext = cur.next
            cur.next = prev
            prev, cur = cur, tmpnext

        lp.next.next = cur
        lp.next = prev
        return dummy.next  
