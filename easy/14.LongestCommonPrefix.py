class Solution:
    def longestCommonPrefix(self, strs: list) -> str:

        if not strs:
            return ''

        shortest = min(strs, key=len)
        for idx, chr_ in enumerate(shortest):
            for others in strs:
                if others[idx] != chr_:
                    return shortest[:idx]
        return shortest


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    strs = ['flower', 'flow', 'flight']
    solution = Solution()
    answer = solution.longestCommonPrefix(strs)
    print(answer)
