class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        1 2 3 4 5 6 7 8

        :type head: ListNode
        :rtype: ListNode
        """
        s1 = head
        if s1 is None:
            return head
        s2 = head.next
        if s2 is None:
            return head
        temp = s2.next
        head = s2

        while True:
            if temp is None:
                s2.next = s1
                s1.next = None
                return head
            s1, s2, temp = self.swapTwo(s1, s2, temp)
            if temp.next is None:
                s1.next = temp
                return head
            s1 = temp
            if s1 is None:
                return head
            s2 = s1.next
            if s2 is None:
                return head
            temp = s2.next

    def swapTwo(self, s1, s2, temp):
        s2.next = s1
        s1.next = temp.next
        return s1, s2, temp


