# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = self.convert_to_number(l1) + self.convert_to_number(l2)
        return self.num_to_list(sum)

    def convert_to_number(self, l):
        s = ""
        while l != None:
            s += str(l.val)
            l = l.next
        return int(s[::-1])
    
    def num_to_list(self, num):
        head = prev = None
        if num <= 0:
            return ListNode(0)
        while num >= 1:
            node = ListNode(num % 10)
            if prev is not None:
                prev.next = node
            prev = node
            if head is None:
                head = prev
            num = num // 10
        return head
