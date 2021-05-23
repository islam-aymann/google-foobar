def answer(l):
    codes = list()
    i = len(l) - 1
    while i:
        num = l[i]

        j = i - 1
        while j > -1:
            den = l[j]

            k = j - 1
            while k > -1:
                rem = l[k]

                d1 = float(num) / float(den)
                d2 = float(den) / float(rem)
                if d1.is_integer() and d2.is_integer():
                    codes.append([rem, den, num])

                k -= 1
            j -= 1
        i -= 1

    return len(codes)


def answer2(l):
    if len(set(l)) == 1:
        return 1
    codes = list()
    for i, n1 in enumerate(l):
        for j, n2 in enumerate(l[i + 1:]):
            for k, n3 in enumerate(l[j + 2:]):
                d1 = float(n3) / float(n2)
                d2 = float(n2) / float(n1)
                if d1.is_integer() and d2.is_integer() and (n1 != n2 != n3):
                    codes.append([n1, n2, n3])

    return len(codes)


if __name__ == '__main__':
    # print answer([1, 2, 3, 4, 5, 6])
    # print answer([1, 1, 1])
    print answer2([1, 2, 3, 4, 5, 6])
    print answer2([1, 1, 1])
