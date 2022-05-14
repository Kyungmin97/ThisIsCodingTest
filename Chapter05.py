"""
print("03. 음료수 얼려 먹기")

nlist=[]
n=4
m=5

for _ in range(n):
  nlist.append(list(map(int,input())))

dx=[0,0,-1,1]
dy=[-1,1,0,0]
print(nlist)
answer=0

def dfs(x,y):
  print("x,y:",x,y)
  nlist[y][x]=2

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx<0 or ny<0 or nx>=m or ny>=n:
      continue

    if nlist[ny][nx] == 0:
      dfs(nx,ny)

for i in range(n):
  for j in range(m):
    if nlist[i][j]==0:
      answer+=1
      dfs(j,i)

print(answer)
"""  

print("04. 미로 탈출")

from collections import deque

n,m=map(int,input().split())
nlist=[]
for _ in range(n):
  nlist.append(list(map(int,input())))


dx=[0,0,-1,1]
dy=[-1,1,0,0]

q=deque()
q.append((0,0,1))
while q:
  x,y,cnt=q.popleft()
  nlist[y][x]=cnt
  print(x,y,cnt)
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or ny<0 or ny>=n or nx>= m:
      continue
    if nlist[ny][nx]==1:
      q.append((nx,ny,cnt+1))
print(nlist[n-1][m-1])



  
  























