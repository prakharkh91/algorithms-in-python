class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # No nodes
        if not head:
            return head
        first = head
        node = head
        second = first.next

        # One Node
        if second is not None:
            head = second
        else:
            return head

        while node is not None and node.next is not None:
            third = second.next
            


        return head

