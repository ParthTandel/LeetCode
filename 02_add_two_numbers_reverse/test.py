from sol import Solution, ListNode

def main():

    l1 = ListNode(1)

    l2 = ListNode(9)
    l2.next = ListNode(9)

    s = Solution()
    s.addTwoNumbers(l1, l2)


main()