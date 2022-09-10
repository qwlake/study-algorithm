from collections import deque


class Node:
    sheep = 0

    def __init__(self, parent, curr, children):
        self.parent, self.curr, self.children = parent, curr if curr == 1 else -1, children

    def __repr__(self):
        return f"{self.curr}-{self.children}"


def solution(info, edges):
    nodes = [Node(-1, info[i], []) for i in range(len(info))]
    for curr, child in edges:
        nodes[curr].children.append(child)
        nodes[child].parent = curr

    sheep = 0
    visit = [0] * len(info)
    visit[0] = 1
    q = deque([[0]])
    while q:
        nexts = []
        for i in q.popleft():
            visit[i] += 1
            if nodes[i].curr == -1:
                sheep += 1
            elif Node.sheep + 1 < 0:
                pass
            else:
                if visit[i] <= 1:
                    nexts.append(i)
                continue
            Node.sheep += nodes[i].curr

            for child in nodes[i].children:
                nexts.append(child)
        if nexts:
            q.append(nexts)

    return sheep


if __name__ == "__main__":
    print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
                   [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))  # 5
    print(solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
                   [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]]))  # 5
