def answer(s):
    s = s.replace(' ', '').replace('-', '')
    co = int()

    # for i in range(len(s)):
    #     if s[i] == '>':
    #         for char in s[i:]:
    #             if char == '<':
    #                 co += 2

    # or
    for i, c1 in enumerate(s):
        if c1 == '>':
            for c2 in s[i:]:
                if c2 == '<':
                    co += 2

    return co


if __name__ == '__main__':
    print answer('>----<')
    print answer('--->-><-><-->-')
    print answer('<<>><')
