class Solution:

    def threeSum(self, nums: list) -> list:

        if nums == [] or nums == [0]:
            return []

        nums = sorted(nums)


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [-1, 0, 1, 2, -1, -4]

    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)
