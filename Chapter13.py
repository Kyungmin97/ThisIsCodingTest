"""
print("15. 특정 거리의 도시 찾기")
from collections import deque
INF=int(1e9)

def bfs(n,depth):
  visited[n]=True
  distance[n]=depth
  q.append([n,depth])

  while q:
    x=q.pop()
    for i in graph[x[0]]:
      if visited[i]==True:
        continue
      visited[i]=True
      distance[i]=x[1]+1
      q.append([i,x[1]+1])
    

n,m,k,x=map(int,input().split())
q=deque()
graph=[[]*(n+1) for _ in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)
for _ in range(m):
  a,b=map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

bfs(x,0)

if k in distance: 
  for i in range(n+1):
    if distance[i]==k:
      print(i)
else:
  print(-1)
"""
"""
print("16. 연구소")
def dfs(x,y,depth):
  visited[y][x]==False
  


n,m=map(int,input().split())
graph=[]
visited=[[False]*(m+1) for _ in range (n+1)]
for _ in range(n):
  graph.append(list(map(int,input().split())))
print(graph)

for i in range(n*m):
  for j in range(i+1,n*m):
    for k in range(j+1,n*m):
      x1,y1=i%m,i//m
      x2,y2=j%m,j//m
      x3,y3=k%m,k//m
      if graph[y1][x1]>0 or graph[y2][x2]>0 or graph[y3][x3]>0:
        continue
      print(x1,y1,"+++",x2,y2,"+++",x3,y3)
"""    
"""
print("17. 경쟁적 전염")

dx=[0,0,1,-1]
dy=[-1,1,0,0]

def dfs(x,y,num):
  graph2[y][x]=num
  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]
    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    if graph2[ny][nx]!=0:
      continue
    graph2[ny][nx]=num

n,k=map(int,input().split())
graph=[]
for i in range(n):
  graph.append(list(map(int,input().split())))
s,ansx,ansy=map(int,input().split())


for _ in range(s):
  graph2=[[0]*n for _ in range(n)]
  for num in range(1,k+1):
    for i in range(n):
      for j in range(n):
        if graph[j][i]==num:
          dfs(i,j,num)
  graph=graph2[:]

print(graph[ansy-1][ansx-1])
"""

































































