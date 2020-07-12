
class Solution:

    def __init__(self):
        self.Rom2Int = {'I': 1,
                        'V': 5,
                        'X': 10,
                        'L': 50,
                        'C': 100,
                        'D': 500,
                        'M': 1000
                        }

    def romanToInteger(self, s: str) -> int:

        int_ = 0
        if set(s) == 'I':
            for idx, r in enumerate(s):
                int_ += self.Rom2Int[r]

        else:
            for idx, r in enumerate(s):
                if len(s[idx:]) >= 2:
                    if self.Rom2Int[r] >= self.Rom2Int[s[idx + 1]]:
                        int_ += self.Rom2Int[r]
                    else:
                        int_ -= self.Rom2Int[r]
                else:
                    int_ += self.Rom2Int[r]

        return int_


if __name__ == '__main__':
    s = 'MCMXCIV'
    solution = Solution()
    answer = solution.romanToInteger(s)
    print(answer)
