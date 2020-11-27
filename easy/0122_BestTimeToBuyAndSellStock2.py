class Solution:

    def maxProfit_peak_valley(self, prices: list) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        valley = prices[0]
        total_profit = 0

        if prices == []:
            return total_profit

        for price in prices:
            if price < valley:
                valley = price
            elif price > valley:
                total_profit += price - valley
                valley = price
        return total_profit

    def maxProfit_one_pass(self, prices: list) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        total_profit = 0

        if prices == []:
            return total_profit

        for i in range(1, len(prices), 1):
            if prices[i] > prices[i - 1]:
                total_profit += prices[i] - prices[i -1]
        return total_profit


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    answer = solution.maxProfit_one_pass(prices)
    print(answer)

    prices = [1, 2, 3, 4, 5]
    solution = Solution()
    answer = solution.maxProfit_one_pass(prices)
    print(answer)

    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    answer = solution.maxProfit_one_pass(prices)
    print(answer)
