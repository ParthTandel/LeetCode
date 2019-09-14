# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    @staticmethod
    def listprint(x):
        while x:
            print(x.val)
            x = x.next





class Solution(object):
    def len_list(self, l):
        count = 0
        while l != None:
            count = count + 1
            l = l.next
        return count

    def add_num_rec(self, l1, l2, l):
        if l1.next == None:
            sum = l1.val + l2.val
            carry = int(sum / 10)
            l.next = ListNode(sum % 10)
            return carry

        l.next = ListNode(0)
        sum = l1.val + l2.val + self.add_num_rec(l1.next, l2.next, l.next)
        carry = int(sum/10)
        l.next.val = (sum % 10)
        return carry



    def addTwoNumbers(self, l1, l2):
        diff = self.len_list(l1) - self.len_list(l2)
        l = s = ListNode(0)
        d = abs(diff)

        while d > 0:
            l.next = ListNode(0)
            l = l.next
            d = d - 1
        
        if diff < 0:
            l.next = l1
            l1 = s
            l1 = l1.next
        else:
            l.next = l2
            l2 = s
            l2 = l2.next


        l = ListNode(0)
        carry = self.add_num_rec(l1,l2,l)
        if carry != 0:
            l.val = carry
        else:
            l = l.next
        
        return l