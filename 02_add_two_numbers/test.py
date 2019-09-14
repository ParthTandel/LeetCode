from sol import Solution, ListNode

def main():
    #  (9 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    # l1 = ListNode(9)
    # l1.next = ListNode(7)
    # l1.next.next = ListNode(4)
    # l1.next.next.next = ListNode(3)
    # # l1.next.next.next.next = ListNode(3)

    # l2 = ListNode(5)
    # l2.next = ListNode(6)
    # l2.next.next = ListNode(4)


    l1 = ListNode(1)

    l2 = ListNode(9)
    l2.next = ListNode(9)

    s = Solution()
    s.addTwoNumbers(l1, l2)


main()