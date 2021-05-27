from collections import deque


def solution(_map):
    rows, cols = len(_map), len(_map[0])
    k = 1  # number of walls
    directs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    walls = [[-1 for j in range(cols)] * cols for i in range(rows)]

    q = deque()
    q.append([0, 0, k, 0])  # row, col, walls, distance

    while len(q):
        cr, cc, cw, cd = q.popleft()
        if cr == rows - 1 and cc == cols - 1:
            return cd + 1

        if _map[cr][cc] == 1:
            cw -= 1

        for direct in directs:
            nr, nc = cr + direct[0], cc + direct[1]

            if 0 <= nr < rows and 0 <= nc < cols and walls[nr][nc] < cw:
                q.append([nr, nc, cw, cd + 1])
                walls[nr][nc] = cw

    return -1


if __name__ == '__main__':
    l1 = [
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0]
    ]
    l2 = [
        [0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0]
    ]

    ls = [l1, l2]
    print 'solution(l1)', ':\n', solution(l1)

    # print 'solution(l2)', ':\n', solution(l2)
