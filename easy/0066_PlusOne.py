class Solution:

    def plusOne(self, digits: list) -> list:
        '''
        Time Complexity = O(N)
        Space Complexity = O(N)
        '''
        for i in range(-1, -len(digits) - 1, -1):
            if digits[i] == 9:
                digits[i] = 0
                if i == -len(digits):
                    digits.insert(0, 1)
                    return digits
            else:
                digits[i] += 1
                return digits


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    digits = [1, 2, 3]
    solution = Solution()
    answer = solution.plusOne(digits)
    print(answer)

    digits = [9]
    solution = Solution()
    answer = solution.plusOne(digits)
    print(answer)
