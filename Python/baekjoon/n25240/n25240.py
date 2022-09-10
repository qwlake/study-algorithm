import sys
from collections import defaultdict

input = sys.stdin.readline


PERMISSION_MAP = {
    'X': 1,
    'W': 2,
    'R': 4,
}


class Permission:
    def __init__(self, p: str):
        self.o, self.g, self.e = map(int, list(p))

    def is_possible(self):
        pass


def solution():
    u, f = map(int, input().split())
    users = defaultdict(set)
    files = {}
    for _ in range(u):
        user_info = input().split()
        if len(user_info) > 1:
            users[user_info[0]].add(user_info[1:].split(','))
        else:
            users[user_info[0]].add(user_info[0])
    for _ in range(f):
        file_name, permission, owner, owned_group = input().split()
        files[file_name] = {'permission': Permission(permission), 'owner': owner, 'owned_group': owned_group}

    for _ in range(int(input())):
        user_name, file_name, operation = input().split()

        PERMISSION_MAP[operation]

        file_info = files[file_name]
        p = file_info['permission']
        if user_name == file_info['owner'] and p.o:
            print(1)




if __name__ == '__main__':
    solution()
