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
n = int(input())
a = list()
for i in range(n):
	x, y = input().split()
	y = int(y)
	if x == "S":
		a.append(y + 0)
	if x == "H":
		a.append(y + 13)
	if x == "C":
		a.append(y + 26)
	if x == "D":
		a.append(y + 39)
for i in range(1, 53):
	if not (i in a):
		if i <= 13:
			print("S {}".format(i - 0))
		elif i <= 26:
			print("H {}".format(i - 13))
		elif i <= 39:
			print("C {}".format(i - 26))
		else:
			print("D {}".format(i - 39))


"""
C問題
"""

n = int(input())
a = list() #空のリスト

for i in range(n):
	b, f, r, v = map(int,input().split())

	


"""
D問題
"""