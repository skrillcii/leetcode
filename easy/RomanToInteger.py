
class Solution:

    Pairs = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            }

    def romanToInteger(self, s:str) -> int:

        import ipdb
        ipdb.set_trace()

        return False

if __name__ == '__main__':
    s = 'XI'
    solution = Solution()
    answer = solution.romanToInteger(s)
    print(answer)
