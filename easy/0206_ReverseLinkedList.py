class Node:

    def __init__(self, val=0, next_=None):
        self.val = val
        self.next = next_


class Solution:

    def reverseList(self, head) -> list:
        '''
        Time Complexity = O(N)
        Space Complexity = O(1)
        '''
        prev = None
        while head:
            temp = head
            head = head.next
            temp.next = prev
            prev = temp
        return prev


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    solution = Solution()
    answer = solution.reverseList(node1)
    print(answer)
