n = int(input())
a1 = [[0 for i in range(10)] for j in range(3)] #空のリスト
a2 = [[0 for i in range(10)] for j in range(3)] #空のリスト
a3 = [[0 for i in range(10)] for j in range(3)] #空のリスト
a4 = [[0 for i in range(10)] for j in range(3)] #空のリスト

for i in range(n):
	b, f, r, v = map(int,input().split())
	if b == 1:
		a1[f-1][r-1] = v
		print(a1)

	elif b == 2:
		a2[f-1][r-1] = v
		print(a2)

	elif b == 3:
		a3[f-1][r-1] = v
		print(a3)

	else:
		a4[f-1][r-1] = v
		print(a4)

print(a1)
print('#'*10)
print(a2)
print('#'*10)
print(a3)
print('#'*10)
print(a4)