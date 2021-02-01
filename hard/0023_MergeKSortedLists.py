class ListNode:

    def __init__(self, val, next_=None):
        self.val = val
        self.next = next_


class LinkList:

    def __init__(self, list_: list):
        self.head = ListNode(list_[0])
        tail = self.head
        i = 1
        while i < len(list_):
            tail.next = ListNode(list_[i])
            tail = tail.next
            i += 1


class Solution:

    def mergeKLists(self, lists: list) -> ListNode:

        def merge2Lists(l1: LinkList, l2: LinkList) -> ListNode:
            if l1 is None:
                return l2
            elif l2 is None:
                return l1
            elif l1.val < l2.val:
                l1.next = merge2Lists(l1.next, l2)
                return l1
            else:
                l2.next = merge2Lists(l1, l2.next)
                return l2

        for i in range(0, len(lists) - 1):
            lists[i + 1] = merge2Lists(lists[i], lists[i + 1])
        return lists[-1]


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    list_ = [[1, 4, 5], [1, 3, 4], [2, 6]]
    lists = [LinkList(x).head for x in list_]
    solution = Solution()
    answer = solution.mergeKLists(lists)
    print(answer)
