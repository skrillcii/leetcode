
def reverse(x):
    '''
    :type x: int
    :rtype: int
    '''

    if abs(x)>2**31-1: return 0

    else:
        string = str(x)
        if x >= 0:
            y = string[::-1]
        else:
            temp1 = string[1:]
            temp2 = temp1[::-1]
            y = int(temp2) * -1

        if abs(int(y)) >= 2**31-1: return 0
        else: return int(y)



if __name__ == '__main__':
    x = -123
    solution = reverse(x)
    print(solution)

