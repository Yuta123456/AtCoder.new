n = int(input())
ans = 0
for i in range(n):
    l, r  = list(map(int, input().split()))
    ans += 1 + (r - l)
print(ans)