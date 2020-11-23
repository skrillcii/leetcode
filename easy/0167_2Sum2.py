class Solution:

    def twoSum2(self, numbers: list, target: list):

        i, j = 0, -1
        while True:
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + len(numbers) + 1]
            elif numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    numbers = [2, 7, 11, 15]
    target = 9

    numbers = [2, 3, 4]
    target = 6

    numbers = [-1, 0]
    target = -1
    solution = Solution()
    answer = solution.twoSum2(numbers, target)
    print(answer)
