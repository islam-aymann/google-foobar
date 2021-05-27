import itertools


def nums_to_num(nums):
    return int("".join([str(num) for num in nums]))


def div_by_3(num):
    return not num % 3


def solution(l):
    if not l:
        return 0

    for i in range(len(l), 0, -1):
        for nums in sorted(itertools.permutations(l, i), reverse=True):
            num = nums_to_num(nums)
            if div_by_3(num):
                return num
    return 0


if __name__ == '__main__':
    ls = [[3, 1, 4, 1], [3, 1, 4, 1, 5, 9]]
    # ls = [[3, 1, 4, 1, 5, 9]]
    for l in ls:
        print "solution({}):\n".format(l), solution(l)
