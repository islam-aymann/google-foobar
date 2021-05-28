import itertools


def solution(num_buns, num_required):
    keys = [[] for num in range(num_buns)]
    copies_per_key = num_buns - num_required + 1
    for key, bunnies in enumerate(
            itertools.combinations(range(num_buns), copies_per_key)):
        for bunny in bunnies:
            keys[bunny].append(key)

    return keys


if __name__ == '__main__':
    # print solution(2, 1)
    # [
    #   [0],
    #   [0]
    # ]
    print solution(2, 2)
    # [
    #   [0],
    #   [1]
    # ]
    # print solution(3, 2)
    # [
    #   [0, 1],
    #   [0, 2],
    #   [1, 2]
    # ]
    # print solution(4, 4)
    # [
    #   [0],
    #   [1],
    #   [2],
    #   [3]
    # ]
    print solution(5, 3)
    # [
    #  [0, 1, 2, 3, 4, 5],
    #  [0, 1, 2, 6, 7, 8],
    #  [0, 3, 4, 6, 7, 9],
    #  [1, 3, 5, 6, 8, 9],
    #  [2, 4, 5, 7, 8, 9]
    # ]
