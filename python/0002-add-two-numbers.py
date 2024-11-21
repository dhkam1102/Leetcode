# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = l1, l2

        dummy = ListNode()
        tail = dummy
        round = 0

        while head1 or head2:
            val1 = head1.val if head1 else 0
            val2 = head2.val if head2 else 0
            
            total = val1 + val2 + round
            quo = total % 10
            round =  1 if total >= 10 else 0

            temp = ListNode(quo)
            tail.next = temp
            tail = tail.next
            head1 = head1.next if head1 else None
            head2 = head2.next if head2 else None

        if round == 1:
            tail.next = ListNode(1)
        
        return dummy.next









