
class Solution:
    def isAlienSorted(self, words: list(), order: str) -> bool:

        for i in range(len(words) - 1):
            word_head = words[i]
            word_next = words[i + 1]
            for j in range(min(len(word_head), len(word_next))):
                if order.index(words[i][j]) != order.index(words[i + 1][j]):
                    if order.index(words[i][j]) > order.index(words[i + 1][j]):
                        return False
                    break
            else:
                if len(word_head) > len(word_next):
                    return False
        return True

    # Optimized Solution
    # def isAlienSorted(self, words, order):
    #     m = {c: i for i, c in enumerate(order)}
    #     words = [[m[c] for c in w] for w in words]
    #     import ipdb
    #     ipdb.set_trace()
    #     return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))


if __name__ == '__main__':

    # words = ["hello", "leetcode"]
    # order = "hlabcdefgijkmnopqrstuvwxyz"

    # words = ["word", "world", "row"]
    # order = "worldabcefghijkmnpqstuvxyz"

    # words = ["apple", "app"]
    # order = "abcdefghijklmnopqrstuvwxyz"

    # words = ["kuvp", "q"]
    # order = "ngxlkthsjuoqcpavbfdermiywz"

    words = ["fxasxpc", "dfbdrifhp", "nwzgs", "cmwqriv", "ebulyfyve",
             "miracx", "sxckdwzv", "dtijzluhts", "wwbmnge", "qmjwymmyox"]
    order = "zkgwaverfimqxbnctdplsjyohu"

    solution = Solution()
    answer = solution.isAlienSorted(words, order)
    print(answer)
