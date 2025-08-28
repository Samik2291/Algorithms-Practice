# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head, prev = None):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        og = head
        reverse = None
        while og:
            og, reverse, reverse.next = og.next, og, reverse
        return reverse
        