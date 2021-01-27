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
        Space Complexity = O(N)
        '''
        return None

    def removeNthFromEnd_value_shifting(self, head: ListNode, n: int) -> ListNode:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
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
            return i
        index(head)
        return head.next


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    n = 2
    list_ = [1, 2, 3, 4, 5]
    head = LinkedList(list_).head
    solution = Solution()
    answer = solution.removeNthFromEnd_recursive_shift(head, n)
    print(answer)

    n = 1
    list_ = [1]
    head = LinkedList(list_).head
    solution = Solution()
    answer = solution.removeNthFromEnd_recursive_shift(head, n)
    print(answer)

    n = 1
    list_ = [1, 2]
    head = LinkedList(list_).head
    solution = Solution()
    answer = solution.removeNthFromEnd_recursive_shift(head, n)
    print(answer)
