class Solution:

    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        '''
        Time Complexity: O(N+M)
        Space Complexity: O(1)
        '''
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]
        return nums1

    def merge_concise(self, nums1, m, nums2, n):
        '''
        Time Complexity: O(N+M)
        Space Complexity: O(1)
        '''
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    solution = Solution()
    answer = solution.merge(nums1, 3, nums2, len(nums2))
    print(answer)

    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 3, 6]
    solution = Solution()
    answer = solution.merge(nums1, 3, nums2, len(nums2))
    print(answer)

    nums1 = [0]
    nums2 = [1]
    solution = Solution()
    answer = solution.merge(nums1, 0, nums2, len(nums2))
    print(answer)

    nums1 = [2, 0]
    nums2 = [1]
    solution = Solution()
    answer = solution.merge(nums1, 1, nums2, len(nums2))
    print(answer)

    nums1 = [4, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    solution = Solution()
    answer = solution.merge(nums1, 3, nums2, len(nums2))
    print(answer)

    nums1 = [0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 4, 5]
    solution = Solution()
    answer = solution.merge(nums1, 0, nums2, len(nums2))
    print(answer)
