class Solution:

    def maxProfit_1st_trial(self, prices: list) -> int:
        '''
        Time Complexity: O(NlogN)
        Space Complexity: O(1)
        '''
        if prices == []:
            return 0

        prefix_profit = []
        for i, pi in enumerate(prices):
            max_ = 0
            for j, pj in enumerate(prices[i + 1:]):
                if j > i:
                    diff = pj - pi
                    if diff > max_:
                        max_ = diff
            prefix_profit.append(max_)
        return max(prefix_profit)

    def maxProfit_2nd_trial(self, prices: list) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if prices == []:
            return 0

        max_profit = 0
        min_price = max(prices)

        for price in prices:
            min_price = min(price, min_price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        return max_profit

    def maxProfit_minimal(self, prices: list) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        buy, ans = float('inf'), 0
        for p in prices:
            buy, ans = min(buy, p), max(ans, p-buy)
        return ans


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    answer = solution.maxProfit_2nd_trial(prices)
    print(answer)

    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    answer = solution.maxProfit_2nd_trial(prices)
    print(answer)
