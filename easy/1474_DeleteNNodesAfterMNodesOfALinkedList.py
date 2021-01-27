class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, list_: list) -> ListNode:
        self.head = ListNode(list_[0])
        tail = self.head
        i = 1
        while i < len(list_):
            tail.next = ListNode(val=list_[i])
            tail = tail.next
            i += 1


class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''
        counter = 0
        slow = fast = head
        while fast is not None:
            if counter < m:
                slow = fast
                fast = fast.next
                counter += 1
            elif m <= counter < m + n:
                slow.next = fast.next
                fast = fast.next
                counter += 1
            else:
                counter = 0
        return head


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    head = LinkedList(list_).head
    m, n = 2, 3
    solution = Solution()
    answer = solution.deleteNodes(head, m, n)
    print(answer)

    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    head = LinkedList(list_).head
    m, n = 1, 3
    solution = Solution()
    answer = solution.deleteNodes(head, m, n)
    print(answer)

    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    head = LinkedList(list_).head
    m, n = 3, 1
    solution = Solution()
    answer = solution.deleteNodes(head, m, n)
    print(answer)

    list_ = [9, 3, 7, 7, 9, 10, 8, 2]
    head = LinkedList(list_).head
    m, n = 1, 2
    solution = Solution()
    answer = solution.deleteNodes(head, m, n)
    print(answer)
