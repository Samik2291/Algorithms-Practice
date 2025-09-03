# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        
        reverse, mid = None, slow
        while mid:
            reverse, reverse.next, mid = mid, reverse, mid.next
        
        first = head
        while reverse.next:
            '''
            first_next = first.next
            reverse_next = reverse.next
            reverse.next = first_next
            first.next = reverse
            first = first.next.next
            reverse = reverse_next
            '''
            first.next, first = reverse, first.next
            reverse.next, reverse = first, reverse.next
        return
            

            

        

            

       