
class ListNode():
    def __init__(self, val=None):
        self.val  = val
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


if __name__ == '__main__':

    # import ipdb
    # ipdb.set_trace()

    a = [1, 2, 4]
    b = [1, 3, 4]

    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    solution = Solution()
    answer = solution.mergeTwoLists(l1, l2)
    print(answer)
