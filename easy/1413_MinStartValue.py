class Solution:

    def minStartValue_1st_trail(self, nums: list) -> int:
        i = 1
        while True:
            sum_ = self.loopSum(i, nums)
            if not sum_:
                i += 1
            else:
                return i

    def loopSum(self, sum_, nums):
        for j in range(len(nums)):
            sum_ = sum_ + nums[j]
            if sum_ < 1:
                return False
        else:
            return sum_

    def minStartValue_2nd_trail(self, nums: list) -> int:
        if nums[0] < 0:
            i = -nums[0] + 1
        else:
            i = 1

        while True:
            sum_ = i
            for j in range(len(nums)):
                sum_ = sum_ + nums[j]
                if sum_ < 1:
                    i += -sum_ + 1
                    break
            if sum_ >= 1:
                return i

    def minStartValue_prefix_sum(self, nums: list) -> int:
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        min_ = min(prefix_sum)
        if min_ <= 0:
            return -min(prefix_sum) + 1
        else:
            return min(prefix_sum)


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [-3, 2, -3, 4, 2]
    nums = [1, -2, -3]
    nums = [1, 2]

    solution = Solution()
    answer = solution.minStartValue_1st_trail(nums)
    print(answer)
    answer = solution.minStartValue_2nd_trail(nums)
    print(answer)
    answer = solution.minStartValue_prefix_sum(nums)
    print(answer)
