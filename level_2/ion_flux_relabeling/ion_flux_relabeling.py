def process_converter(max_idx, conv):
    pn = -1
    cn = max_idx
    sub = max_idx

    if cn == conv:
        return pn

    pn = cn

    while sub > 1:

        sub /= 2

        left = cn - sub - 1
        right = cn - 1

        if conv == left or conv == right:
            return pn

        if conv < left:
            cn = left
        elif conv > left:
            cn = right

        pn = cn

    return -1


def solution(h, q):
    max_idx = 2 ** h - 1
    return [process_converter(max_idx, conv) for conv in q]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, data, depth=1, height=1):
        if depth >= height:
            return None

        if not self.right:
            self.right = Node(data)
            return self.right
        else:
            right = self.right.add(data, depth + 1, height)
            if not right:
                if not self.left:
                    self.left = Node(data)
                    return self.left
                else:
                    return self.left.add(data, depth + 1, height)
            else:
                return right


class Tree:
    def __init__(self, r, h):
        self.root = r
        self.height = h

    def add(self, data):
        self.root.add(data, 1, self.height)

    def find_parent(self, val, node=None, parent=-1):
        if not node:
            return

        if node.data == val:
            return parent
        else:
            left = self.find_parent(val, node.left, node.data)
            if left:
                return left

            right = self.find_parent(val, node.right, node.data)
            if right:
                return right


def solution2(h, q):
    tree = Tree(Node(2 ** h - 1), h)

    for value in range(2 ** h - 2, 0, -1):
        tree.add(value)

    output = list()
    for i in q:
        parent = tree.find_parent(i, tree.root)
        if parent not in output:
            output.append(parent)

    return output


if __name__ == "__main__":
    # print 'solution(3, [7, 3, 5, 1])', ':\n', solution(3, [7, 3, 5, 1])
    print 'solution(5, [19, 14, 28])', ':\n', solution(5, [19, 14, 28])
