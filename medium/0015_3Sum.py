class Solution:

    def threeSum(self, nums: list) -> list:

        # Do not need this explicit check, it will only go into loops
        # if condition satisfy
        # if nums == [] or nums == [0] or len(nums) <= 2:
        #     return []
        # else:

        nums.sort()
        solutions = []
        for idx, target in enumerate(nums):
            if target > 0:
                break
            elif idx == 0 or nums[idx] != nums[idx - 1]:
                self.twoSum(nums, idx, target, solutions)

        return solutions

    def twoSum(self, nums, idx, target, solutions):

        p1 = idx + 1
        p2 = len(nums) - 1

        while p1 < p2:
            sum_ = nums[p1] + nums[p2] + target
            if sum_ == 0:
                solutions.append([target, nums[p1], nums[p2]])
                p1 += 1
                p2 -= 1
                while p1 < p2 and nums[p1] == nums[p1 - 1]:
                    p1 += 1
            elif sum_ < 0:
                p1 += 1
            elif sum_ > 0:
                p2 -= 1


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)

    nums = [0, 0]
    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)

    nums = [0, 0, 0]
    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)

    nums = [-2, 0, 0, 2, 2]
    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)
