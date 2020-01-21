N = 5
i = None
j = None
k = None
a =[int(input()) for i in range(N)]
print(a)
k=0
for i in range (N-1):
    if ((a[i]+a[i+1]) % 2 == 0) and (a[i]*a[i+1] >100):
        k +=1
print(k)