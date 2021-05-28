def solution(n):
    c = int()
    n = int(n)
    while n > 1:
        if n % 2 == 0:
            n /= 2
        elif n == 3 or n % 4 == 1:
            n -= 1
        else:
            n += 1
        c += 1
    return c


if __name__ == '__main__':
    print solution('4')
    print solution('15')
    print solution('768')
    print solution('1235')
