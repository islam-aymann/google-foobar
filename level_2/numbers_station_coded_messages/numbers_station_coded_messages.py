def answer(l, t):
    p = list()

    w = 1
    while w <= len(l):
        i = 0
        while i + w <= len(l):
            window = l[i: i + w]
            if sum(window) == t:
                p.append([i, i + w - 1])

            i += 1

        w += 1

    return sorted(p)[0] if p else [-1, -1]


if __name__ == '__main__':
    print answer([4, 3, 5, 7, 8], 12)
