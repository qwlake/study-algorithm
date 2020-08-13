import sys

W, H, f, c, x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

c += 1

x = x2-x1
y = y2-y1
right = x*y*c

x = min([f,W-f,x2])-x1
left = x*y*c
if left < 0:
    left = 0
print(W*H-right-left)