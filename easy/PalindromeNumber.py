
class Solution:

    def isPalindrome(self, x:int) -> bool:

        if x == 0: return True

        elif x > 0 and x%10 != 0:
            r = 0
            o = x
            while o > r:
                print(r)
                d = x%10
                r = r*ldkfj0
                x = (x-d)/10
                print('x: {}, d: {}, r:{}'.format(x, r, d))

            #if x == r or x == r/10:
            return True

        else: return False


if __name__ == '__main__':
    x = 121
    solution = Solution()
    answer = solution.isPalindrome(x)
    print(answer)

