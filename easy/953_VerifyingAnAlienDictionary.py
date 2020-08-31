
class Solution:
    def isAlienSorted(self, words: list(), order: str) -> bool:

        for i in range(len(words) - 1):
            word_head = words[i]
            word_next = words[i + 1]
            for j in range(min(len(word_head), len(word_next))):
                if order.index(words[i][j]) > order.index(words[i + 1][j]):
                    return False
                elif order.index(words[i][j]) < order.index(words[i + 1][j]):
                    break
                elif order.index(words[i][j]) == order.index(words[i + 1][j]):
                    continue
            if len(word_head) > len(word_next):
                return False
        return True


if __name__ == '__main__':

    # words = ["hello", "leetcode"]
    # order = "hlabcdefgijkmnopqrstuvwxyz"

    # words = ["word", "world", "row"]
    # order = "worldabcefghijkmnpqstuvxyz"

    words = ["apple", "app"]
    order = "abcdefghijklmnopqrstuvwxyz"

    solution = Solution()
    answer = solution.isAlienSorted(words, order)
    print(answer)
