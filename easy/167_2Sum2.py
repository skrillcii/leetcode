
class Solution:
    def twoSum2(self, nums: list, target: list):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        i, j = 0, -1
        while True:
            if nums[i] + nums[j] == target:
                return [i + 1, j + len(nums) + 1]
            elif nums[i] + nums[j] <= target:
                i += 1
            elif nums[i] + nums[j] >= target:
                j -= 1


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9

    nums = [2, 3, 4]
    target = 6

    nums = [-1, 0]
    target = -1
    solution = Solution()
    answer = solution.twoSum2(nums, target)
    print(answer)
