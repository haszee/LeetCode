# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if list1 == None and list2 == None:
            return list1
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            head = ListNode(-1)
            current = head
            
            while list1 != None and list2 != None:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next  

        if list1 != None:
            current.next = list1
        elif list2 != None:
            current.next = list2
        
        return head.next