import bisect
import math
import sys
input = sys.stdin.readline
#####segfunc######
def segfunc(x,y):    
    return x+y

def init(init_val):
    #set_val
    for i in range(n):
        seg[i+num-1]=init_val[i]    
    #built
    for i in range(num-2,-1,-1) :
        seg[i]=segfunc(seg[2*i+1],seg[2*i+2]) 
    
def update(k,x):
    k += num-1
    seg[k] = x
    while k:
        k = (k-1)//2
        seg[k] = segfunc(seg[k*2+1],seg[k*2+2])
    
def query(p,q):
    if q<=p:
        return ide_ele
    p += num-1
    q += num-2
    res=ide_ele
    while q-p>1:
        if p&1 == 0:
            res = segfunc(res,seg[p])
        if q&1 == 1:
            res = segfunc(res,seg[q])
            q -= 1
        p = p//2
        q = (q-1)//2
    if p == q:
        res = segfunc(res,seg[p])
    else:
        res = segfunc(segfunc(res,seg[p]),seg[q])
    return res

#####単位元######
ide_ele = 0
#input
data = []
n, d, a = map(int, input().split())
x_point = []
for i in range(n):
    x, h = map(int, input().split())
    data.append([x,h])
    x_point.append(x)
x_point.sort()
data.sort()
##初期化
num =2**(n-1).bit_length()
seg=[ide_ele]*2*num
ans = 0
for i in range(n):
    x, h = data[i]
    index = bisect.bisect_left(x_point, x - 2*d)
    sum_damage = query(index, i)
    h -= sum_damage
    count = max(((h+a-1)//a), 0)
    ans += count
    update(i, count * a)
print(ans)