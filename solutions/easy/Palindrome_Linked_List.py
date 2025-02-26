from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev =curr
            curr = nxt
        return prev
    
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast = head
        while fast!=None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        if fast != None:
            slow = slow.next

        slow = self.reverseList(slow)
        fast = head
        while slow != None:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        return True 
