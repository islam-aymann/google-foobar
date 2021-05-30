from math import atan2, sqrt


def dist(pos1, pos2):
    return sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)


def get_mirror(mirror, coordinates, dimensions):
    result = coordinates
    mirror_rotation = [2 * coordinates, 2 * (dimensions - coordinates)]
    if mirror < 0:
        for i in range(mirror, 0):
            result -= mirror_rotation[(i + 1) % 2]
    else:
        for i in range(mirror, 0, -1):
            result += mirror_rotation[i % 2]
    return result


def mirror_view(point, dimensions, distance):
    point_mirrored = list()
    for i in range(len(point)):
        points = list()
        for j in range(-(distance // dimensions[i]) - 1,
                       (distance // dimensions[i] + 2)):
            points.append(get_mirror(j, point[i], dimensions[i]))
        point_mirrored.append(points)
    return point_mirrored


def solution(dimensions, your_position, guard_position, distance):
    mirrored = [mirror_view(your_position, dimensions, distance),
                mirror_view(guard_position, dimensions, distance)]
    result = set()
    angles_distances = dict()
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                beam = atan2((your_position[1] - k), (your_position[0] - j))
                l = dist(your_position, (j, k))
                if [j, k] != your_position and distance >= l:
                    if (beam in angles_distances and angles_distances[beam] > l) \
                            or beam not in angles_distances:
                        if i == 0:
                            angles_distances[beam] = l
                        else:
                            angles_distances[beam] = l
                            result.add(beam)
    return len(result)


if __name__ == '__main__':
    print solution([3, 2], [1, 1], [2, 1], 4)
    print solution([300, 275], [150, 150], [185, 100], 500)

    print dist((1, 1), (3, 3))
