class Solution:

    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        '''
        Time Complexity: O(N+M)
        Space Complexity: O(1)
        '''
        p = -1
        p1 = -1
        p2 = -1

        while nums1[p1] == 0:
            p1 -= 1

        while p2 >= -n:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
            elif nums1[p1] > nums2[p2]:
                temp = nums1[p]
                nums1[p] = nums1[p1]
                nums1[p1] = temp
                p -= 1
            elif nums1[p1] == nums2[p2]:
                nums1[p] = nums2[p2]
                p -= 1
                p2 -= 1
        return nums1


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 3, 6]
    solution = Solution()
    answer = solution.merge(nums1, len(nums1), nums2, len(nums2))
    print(answer)
