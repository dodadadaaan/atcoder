"""
A問題
"""
#解法1
while True:

    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break                           #H = W = 0のとき，何も出力しない
    for i in range(H):
        print("#"*W)    #＃をW回出力（文字列と演算子の組み合わせ）

    print()

#解法2
while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            print("#",end = (""))
        print()
    print()


"""
B問題
"""
while True:

    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if i == 0 or i == H-1 or j == 0 or j == W-1:
                print("#",end = (""))
            else:
                print(".", end = (""))
        print()
    print()

"""
C問題
"""
while True:
    H,W = map(int,input().split())
    if H == 0 and W == 0:
        break
    for i in range(H):
        for j in range(W):
            if (i+j) % 2 == 0:  # line odd & column  
                print("#",end = (""))
            else:
                print(".",end = (""))
        print()
    print()

"""
D問題
"""
#よくわからんのでパス！w
