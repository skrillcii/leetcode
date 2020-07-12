
class Solution:
    def twoSum(self, nums:list, target:list):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        unique = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in unique:
                unique[num] = i
            else:
                return [unique[diff], i]


if __name__ == '__main__':
    nums = [3,3]
    target = 6
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)

