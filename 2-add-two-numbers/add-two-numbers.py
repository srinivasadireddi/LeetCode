#two edge cases
#1: carry number: eg: 8234+589
#2: eg: 6+7= 13, but we write only 3 in the sum list, 1 is carry number, it should be included despite there being no number in front of 6 and 7. 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:

        dummy = ListNode()
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            val1= l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            val3 = val1 + val2+ carry

            carry = val3//10
            val3 = val3%10

            cur.next= ListNode(val3)
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None

        return dummy.next



        