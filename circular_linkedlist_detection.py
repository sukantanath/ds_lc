# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head == None or head.next == None:
            return False
        
        slow = head
        fast = head.next
        
        while (slow != fast):
            
            if (fast == None or fast.next == None):
                return False
            
            slow = slow.next
            fast = fast.next.next 
        
        return True
