n = int(input())
a1 = [[0 for i in range(10)] for j in range(3)] #空のリスト
a2 = [[0 for i in range(10)] for j in range(3)] #空のリスト
a3 = [[0 for i in range(10)] for j in range(3)] #空のリスト
a4 = [[0 for i in range(10)] for j in range(3)] #空のリスト

for i in range(n):
	b, f, r, v = map(int,input().split())
	if b == 1:
		a1[1][] = 