n, q = map(int, input().split())
a = [0 for i in range(n)]
for i in range(q):
    l,r,t = map(int, input().split())
    for j in range(l-1,r):
        a[j] = t
for i in range(n):
    print(a[i])