def answer(start, length):
    row = 1
    cs = 0  # X ^ 0 = X
    while row <= length:
        for i in range(start, start + length - row + 1):
            cs ^= i
        start += length
        row += 1
    return cs


if __name__ == '__main__':
    print 'answer(0, 3)', ':', answer(0, 3)
    print 'answer(17, 4)', ':', answer(17, 4)
