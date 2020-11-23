class Solution:

    def runningSum(self, nums: list) -> list:
        sums = []
        for i in range(len(nums)):
            if i == 0:
                sums.append(nums[i])
            else:
                sums.append(sums[i - 1] + nums[i])
        return sums

if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [1, 2, 3, 4]

    solution = Solution()
    answer = solution.runningSum(nums)
    print(answer)
