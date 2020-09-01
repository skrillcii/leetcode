
def binarian(A):
    output = 0
    for i in A:
        output += 2 ** i
    return output


def solution(A):

    B = []
    binarian_ = binarian(A)

    while binarian_ != 0:
        if binarian_ == 1:
            sqrt = 0
        else:
            sqrt = int(binarian_ ** (0.5))
        binarian_ -= 2 ** sqrt
        B.append(sqrt)
    return len(B)


if __name__ == '__main__':
    A = [1, 0, 2, 0, 0, 2]
    answer = solution(A)
    print(answer)
