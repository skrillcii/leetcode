class Solution:

    def twoSum(self, nums: list, target: list):
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        unique = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff not in unique:
                unique[num] = i
            else:
                return [unique[diff], i]


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)

    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)

    nums = [3, 3]
    target = 6
    solution = Solution()
    answer = solution.twoSum(nums, target)
    print(answer)
