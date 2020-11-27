class Solution:

    def maxProfit2(self, prices: list) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        valley = prices[0]
        total_profit = 0

        if prices == []:
            return max_profit

        for price in prices:
            if price < valley:
                valley = price
            elif price > valley:
                total_profit += price - valley
                valley = price
        return total_profit


if __name__ == '__main__':

    import ipdb
    ipdb.set_trace()

    prices = [7, 1, 5, 3, 6, 4]
    solution = Solution()
    answer = solution.maxProfit2(prices)
    print(answer)

    prices = [1, 2, 3, 4, 5]
    solution = Solution()
    answer = solution.maxProfit2(prices)
    print(answer)

    prices = [7, 6, 4, 3, 1]
    solution = Solution()
    answer = solution.maxProfit2(prices)
    print(answer)
