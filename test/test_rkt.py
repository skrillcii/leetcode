import math


def binarian(A):
    return sum([2 ** i for i in A])


def solution(A):
    B = []
    binarian_ = binarian(A)
    while binarian_ != 0:
        b = int(math.log(binarian_, 2))
        B.append(b)
        binarian_ -= 2 ** b
    return len(B)


if __name__ == '__main__':

    # Array length = [0, 100000]
    # Element range = [0, 10000]

    A = [1, 0, 2, 0, 0, 2]
    A = [10, 10, 10]
    A = [10000, 10000, 10000]
    answer = solution(A)
    print(answer)
