class Solution:

    def threeSum(self, nums: list) -> list:

        if nums == [] or nums == [0]:
            return []

        nums = sorted(nums)
        solutions = []

        for idx, target in enumerate(nums):

            if target > 0:
                break

            p1 = idx + 1
            p2 = -1

            while  nums[p1] < nums[p2]:
                if target == nums[idx - 1]:
                    break

                elif nums[p1] + nums[p2] + target == 0:
                    solutions.append([target, nums[p1], nums[p2]])
                    p1 += 1
                    p2 -= 1

                elif nums[p1] + nums[p2] < target:
                    p1 += 1

                elif nums[p1] + nums[p2] > target:
                    p2 -= 1

        return solutions


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    nums = [-1, 0, 1, 2, -1, -4]

    solution = Solution()
    answer = solution.threeSum(nums)
    print(answer)
