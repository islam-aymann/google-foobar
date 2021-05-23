from collections import Counter


def answer(data, n):
    if not n:
        return list()

    c = Counter(data)

    fl = list()

    for i in data:
        if i not in fl and c[i] <= n:
            fl.append(i)

    return fl


if __name__ == '__main__':
    print answer([1, 2, 3], 0)
    print answer([1, 2, 2, 3, 3, 3, 4, 5, 5], 1)
    print answer([5, 10, 15, 10, 7], 1)
