# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum = 0
        carry = 0
        y = ListNode(0)
        s = y
        while(l1 and l2 ):
            sum = l1.val + l2.val + carry
            carry = sum / 10
            sum = sum % 10
            y.val = sum
            if l1.next == None and l2.next == None and carry == 0:
                break
            elif l1.next == None and l2.next == None:
                y.next = ListNode(carry)
                y = y.next
                break
            
            if l1.next == None:
                l1.next = ListNode(0)
                
            if l2.next == None:
                l2.next = ListNode(0)
            l1 = l1.next
            l2 = l2.next
            y.next = ListNode(0)
            y = y.next
        return s


        