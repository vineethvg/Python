class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        # take the result l3 to head assigned to first node
        head = l3 = ListNode(0)
        # initiate a variable to handle carry
        carry = 0

        # l1 or l2 or carry exists
        while l1 or l2 or carry:
            if l1:
                # assign carry to the l1 value
                carry = carry + l1.val
                # iterate
                l1 = l1.next

            if l2:
                # same goes for l2
                carry = carry + l2.val
                l2 = l2.next

            # assign carry to l3.val
            # update carry
            l3.val = carry % 10
            carry = carry // 10

            if l1 or l2 or carry:
                # assign l3 reference to first node
                # then iterate
                l3.next = ListNode(0)
                l3 = l3.next

        # when loop breaks return head
        return head
