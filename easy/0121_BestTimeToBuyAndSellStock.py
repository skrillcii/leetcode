class Solution:

    def maxProfit(self, prices: list) -> int:
        '''
        Time Complexity: O(N+M)
        Space Complexity: O(1)
        '''
        prefix_profit = []
        for i, pi in enumerate(prices):
            max_ = 0
            for j, pj in enumerate(prices[i + 1:]):
                diff = pj - pi
                if diff > max_:
                    max_ = diff
            prefix_profit.append(max_)
        return max(prefix_profit)


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    answer = solution.maxProfit(prices)
    print(answer)

    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    answer = solution.maxProfit(prices)
    print(answer)
