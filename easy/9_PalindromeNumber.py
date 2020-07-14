
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x > 0 and x % 10 != 0:
            r = 0
            while x > r:
                r = r * 10 + x % 10
                x = (x - x % 10) / 10
            if x == r or x == (r - r % 10) / 10:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    x = 31213
    solution = Solution()
    answer = solution.isPalindrome(x)
    print(answer)

