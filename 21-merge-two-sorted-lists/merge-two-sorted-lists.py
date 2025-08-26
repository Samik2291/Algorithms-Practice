# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        track_list = []
        while list1 or list2:
            if not list1:
                track_list.append(list2)
                list2 = list2.next
                continue
            elif not list2:
                track_list.append(list1)
                list1 = list1.next
                continue

            if list1.val <= list2.val:
                track_list.append(list1)
                list1 = list1.next
            else:
                track_list.append(list2)
                list2 = list2.next
        ret = None
        if track_list:
            for node in reversed(track_list):
                #print node
                next = ret
                ret = node
                ret.next = next
        return ret
        
        