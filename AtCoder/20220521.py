"""
A問題
"""
from re import M


A = int(input())
print(chr(A)) #chr関数は十進数の数字を文字列に変換してくれる！

"""
B問題
"""
N, K = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

A_MAX = max(A)

flag = False

for i in range(K):
    if A[ B[i]-1 ] == M:
        flag = True

if flag:
    print("Yes")
else:
        print("No")