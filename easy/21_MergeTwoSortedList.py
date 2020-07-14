
class ListNode():
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self, head=None):
        self.head = ListNode()

    def get_size(self):
        cur_node = self.head
        self.size = 0
        while cur_node is not None:
            self.size += 1
            cur_node = cur_node.next
        return self.size

    def append(self, data):
        new_node = ListNode(data)
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
        cur_node.next = new_node

    def remove(self, data):
        cur_node = self.head
        while cur_node.next != data:
            cur_node = cur_node.next
        return None

    def find(self, data):
        return None

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next is not None:
            cur_node = cur_node.next
            elems.append(cur_node.data)
        print(elems)


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        import ipdb
        ipdb.set_trace()

        return None


if __name__ == '__main__':

    # import ipdb
    # ipdb.set_trace()

    a = [1, 2, 4]
    b = [1, 3, 4]

    l1 = LinkedList()
    l1.append(1)
    l1.append(2)
    l1.append(4)
    l1.display()

    l2 = LinkedList()
    l2.append(1)
    l2.append(3)
    l2.append(4)
    l2.display()

    solution = Solution()
    answer = solution.mergeTwoLists(l1, l2)
    print(answer)
