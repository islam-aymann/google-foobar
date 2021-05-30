from decimal import getcontext, Decimal

getcontext().prec = 105
sqrt2 = Decimal(2).sqrt()


def nd(n):  # n'
    return int(Decimal((sqrt2 - 1) * n))


def S(n):
    if n == 1:
        return 1

    if n < 1:
        return 0

    return n * nd(n) + n * (n + 1) / 2 - nd(n) * (nd(n) + 1) / 2 - S(nd(n))


def solution(str_n):
    return str(S(int(str_n)))


if __name__ == '__main__':
    print solution('77')
    print solution('5')
    # print solution(10 ** 100)
