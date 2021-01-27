class ListNode:

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


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

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''
        slow = fast = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return head

    def removeNthFromEnd_value_shifting(self, head: ListNode, n: int) -> ListNode:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''

        '''
        LeetCode Post:
            'My first solution is "cheating" a little.
            Instead of really removing the nth node, I remove the nth value.
            I recursively determine the indexes (counting from back),
            then shift the values for all indexes larger than n,
            and then always drop the head.'
        '''

        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next

    def removeNthFromEnd_index_and_remove(self, head: ListNode, n: int) -> ListNode:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''

        '''
        LeetCode Post:
            'In this solution I recursively determine the indexes again,
            but this time my helper function removes the nth node.  It returns two values.
            The index, as in my first solution,
            and the possibly changed head of the remaining list.'
        '''

        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i + 1, (head, head.next)[i + 1 == n]
        return remove(head)[1]

    def removeNthFromEnd_n_ahead(self, head: ListNode, n: int) -> ListNode:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''

        '''
        LeetCode Post:
            'The standard solution, but without a dummy extra node. 
            Instead, I simply handle the special case of removing the head 
            right after the fast cursor got its head start.'
        '''
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    n = 2
    list_ = [1, 2, 3, 4, 5]
    head = LinkedList(list_).head
    solution = Solution()
    answer = solution.removeNthFromEnd_value_shifting(head, n)
    print(answer)

    n = 1
    list_ = [1]
    head = LinkedList(list_).head
    solution = Solution()
    answer = solution.removeNthFromEnd_value_shifting(head, n)
    print(answer)

    n = 1
    list_ = [1, 2]
    head = LinkedList(list_).head
    solution = Solution()
    answer = solution.removeNthFromEnd_value_shifting(head, n)
    print(answer)
