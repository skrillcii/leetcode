class Solution:

    def threeSum(self, nums: list) -> list:

        if nums == [] or nums == [0] or len(nums) < 3:
            return []

        else:
            nums.sort()
            solutions = []
            for idx, target in enumerate(nums):
                if target > 0:
                    break
                elif nums[idx] != nums[idx - 1]:
                    self.twoSum(nums, idx, target, solutions)

        return solutions

    def twoSum(self, nums, idx, target, solutions):

        p1 = idx + 1
        p2 = len(nums) - 1

        while nums[p1] < nums[p2]:
            if nums[p1] + nums[p2] + target == 0:
                solutions.append([target, nums[p1], nums[p2]])
                p1 += 1
                p2 -= 1

            elif nums[p1] + nums[p2] + target < 0:
                p1 += 1

            elif nums[p1] + nums[p2] + target > 0:
                p2 -= 1

if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [0, 0]
    nums = [0, 0, 0]

    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)
