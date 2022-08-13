'''
# Program: Equalise
Chef has two numbers AA and BB.

In one operation, Chef can choose either AA or BB and multiply it by 22.

Determine whether he can make both AA and BB equal after any number (possibly, zero) of moves.

'''


from sys import stdin
from collections import deque
from math import log2

n = int(stdin.readline())
x = deque(list(map(int, stdin.readline().split())) for i in range(0, n))

for i in range(0, len(x)):
    a = x.popleft()
    v = [print("YES") if log2((max(a)/min(a))).is_integer() else print("NO")]