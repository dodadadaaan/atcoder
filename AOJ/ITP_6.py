"""
A問題
"""
n = int(input())
a = map(int,input().split())

#int型の入力をlist型に
a_l = list(a) 

#listの中身を逆順に
a_l.reverse() 

#listの出力
for i, elem in enumerate(a_l):  #listの要素とカウンタ同時取得
    if i > 0:
        print(" ", end = "")   # i が 0 より大きいとき、つまり最初の要素ではないとき空白を出力
    print(elem, end = "")
print()   # 改行を出力


"""
B問題
"""



"""
C問題
"""

"""
D問題
"""