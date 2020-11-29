class Solution:

    def numIdenticalPairs(self, nums: list) -> int:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        counter = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    counter += 1
        return counter


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [1, 2, 3, 1, 1, 3]
    solution = Solution()
    answer = solution.numIdenticalPairs(nums)
    print(answer)

    nums = [1, 1, 1, 1]
    solution = Solution()
    answer = solution.numIdenticalPairs(nums)
    print(answer)

    nums = [1, 2, 3]
    solution = Solution()
    answer = solution.numIdenticalPairs(nums)
    print(answer)
