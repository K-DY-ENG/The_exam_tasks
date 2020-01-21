N = int(input())
a = []
max = 0
for i in range (N):
	a.append(int(input()))

b = [0]*18

for i in range(N):
		s = (a[i] % 10 + (a[i] //10)%10)
		b[s-1] += 1 

for i in range (18):
	if max < b[i]:
		max = b[i]

print(b.index(max)+1)