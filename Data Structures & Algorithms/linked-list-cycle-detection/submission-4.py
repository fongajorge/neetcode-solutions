# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        if head.next == None:
            return False

        slow = head
        fast = head.next

        while fast != None:
            if slow == fast:
                return True
            
            slow = slow.next

            if fast and fast.next:
                fast = fast.next.next
            else:
                break
        
        return False
            