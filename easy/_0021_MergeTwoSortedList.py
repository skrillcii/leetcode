class ListNode():

    def __init__(self, val=None, next_=None):
        self.val = val
        self.next = next_


class LinkedList():

    def __init__(self, list_: list):
        self.head = ListNode(val=list_[0])
        tail = self.head
        i = 1
        while i < len(list_):
            tail.next = ListNode(val=list_[i])
            tail = tail.next
            i += 1


class Solution:

    def mergeTwoLists_recursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists_recursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists_recursive(l1, l2.next)
            return l2

    def mergeTwoLists_iterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode()
        while l1.val is not None and l2.val is not None:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    list_1 = [1, 2, 4]
    list_2 = [1, 3, 4]
    l1 = LinkedList(list_1)
    l2 = LinkedList(list_2)
    solution = Solution()
    answer = solution.mergeTwoLists_recursive(l1, l2)
    print(answer)
