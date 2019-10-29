print('введите кол-во друзей которые придут')
n=int(input())
b = [[0] * 3 for i in range(n)]
k=0
for i in range(n):
    b[i] = [int(a) for a in input().split()]
    if b[i][1]>k:
        k=b[i][1]
# n кол-во друзей, k - макс время
s = [[0] * n for i in range(k)]
for i in range(n):
    if b[i][1]-b[i][0] == 1:
        s[b[i][0]][i]=b[i][2]+1
    else:
        while b[i][0]<b[i][1]:
            s[b[i][0]][i]=b[i][2]+1
            b[i][0]=b[i][0]+1
sx=[int(0) for i in range(k)]
k1=0 #макс кол-во друзей в промежуток времени
for i in range(k):
    for j in range(n):
        sx[i]=int(sx[i])+s[i][j]
    if k1 < sx[i]:
        k1 = sx[i]
print(k1) 

