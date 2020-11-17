class Solution:

    def removeDuplicates(self, nums: list) -> int:

        if not nums:
            return 0, []

        i, j = 0, 1
        while j != len(nums):
            if nums[i] == nums[j]:
                j += 1
            else:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
        length = i + 1
        return length, nums[:i + 1]


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [1, 1, 2]
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums = None

    solution = Solution()
    answer = solution.removeDuplicates(nums)
    print(answer)
