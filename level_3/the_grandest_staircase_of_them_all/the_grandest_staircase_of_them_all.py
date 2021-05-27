def solver(height, left, cache):
    if cache[height][left]:
        return cache[height][left]

    if not left:
        return 1

    if left < height:
        return 0

    value = solver(height + 1, left - height, cache) + \
        solver(height + 1, left, cache)

    cache[height][left] = value
    return value


def solution(n):
    cache = [[0 for i in range(n + 2)] for j in range(n + 2)]
    return solver(1, n, cache) - 1


if __name__ == '__main__':
    # print answer(5)
    print solution(7)
