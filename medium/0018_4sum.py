class Solution:

    def fourSum(self, nums: list, target: int) -> list:

        if nums == []:
            return []

        # return quadruplets


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    answer = solution.fourSum(nums, target)
    print(answer)
