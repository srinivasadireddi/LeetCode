# TC: O(n)
# SC:O(1)

# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next

# class Solution:
#     def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
#         start3= ListNode()
#         p3= ListNode(val=None)
#         # if(list1 or list1.val<=list2.val):
#         if(list1==None and list2==None):
#             start3= None
#             return start3
        
#         elif(list1!=None and list2==None):
#             start3=list1
#             p3=list1
#             list1=list1.next
#         elif(list2!=None and list1==None):
#             start3=list2
#             p3=list2
#             list2=list2.next
#         elif(list1 and list2):
#             if(list1.val<=list2.val):
#                 start3=list1
#                 p3=list1
#                 list1=list1.next
#             # elif(list2 or list2.val<list1.val):
#             elif(list2.val<list1.val):
#                 start3=list2
#                 p3=list2
#                 list2=list2.next
#         # while(list1!=None or list2!=None):
#         #     if(list1 or list1.val<=list2.val):
#         while(list1 or list2):
#             if(list1!=None and list2==None):
#                 p3.next = list1
#                 list1=list1.next
#                 p3=p3.next
#             elif(list2!=None and list1==None):
#                 p3.next = list2
#                 list2=list2.next
#                 p3=p3.next
#             elif(list1 and list2):
#                 if(list1.val<=list2.val):
#                     p3.next = list1
#                     list1=list1.next
#                     p3=p3.next
#             # elif(list2 or list2.val<list1.val):
#                 elif(list2.val<list1.val):
#                     p3.next = list2
#                     list2=list2.next
#                     p3=p3.next
#         return start3

#Less wordy solution:
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur=cur.next
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next