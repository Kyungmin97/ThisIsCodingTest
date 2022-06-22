"""
print("37. 플로이드")

INF=int(1e9)
n=int(input())
m=int(input())
graph=[[INF]*(n+1) for _ in range(n+1)]
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b,c=map(int,input().split())
  if c<graph[a][b]:
    graph[a][b]=c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b]==INF:
      print("0", end=" ")
    else:
      print(graph[a][b],end=" ")
  print()
"""
##다익스트라
"""
import heapq
import sys
input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
distance=[INF] * (n+1)

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))

def dijkstra(start):
  q=[]
  heapq.heappush(q,(0,start))
  distance[start]=0
  while q:
    dist,now=heapq.heappop(q)
    if distance[now]<dist:
      continue
    for i in graph[now]:
      cost=dist+i[1]
      if cost<distance[i[0]]:
        distance[i[0]]=cost
        heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INFINITY")
  else:
    print(distance[i])

"""
"""
print("38. 정확한 순위")

INF=int(9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b=map(int,input().split())
  if 1<graph[a][b]:
    graph[a][b]=1
print(graph)

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
print(graph)

result=0
for a in range(1,n+1):
  count=0
  for b in range(1,n+1):
    if graph[a][b]!=INF or graph[b][a]!=INF:
      count+=1
  if count==n:
    result+=1
print(graph)
"""

"""
print("39. 화성 탐사")
INF=int(1e9)
def dfs(x,y):

  for i in range(4):
    nx=x+dx[i]
    ny=y+dy[i]

    if nx<0 or ny<0 or nx>=n or ny>=n:
      continue
    
    elif dp[ny][nx] >= graph[ny][nx]+dp[y][x]:
      dp[ny][nx] = graph[ny][nx]+dp[y][x]
      dfs(nx,ny)


dx=[-1,1,0,0]
dy=[0,0,-1,1]

T=int(input())
for _ in range(T):
  n=int(input())
  graph=[]
  dp=[[INF]*n for i in range(n)]
  
  for _ in range(n):
    graph.append(list(map(int,input().split())))
  dp[0][0]=graph[0][0]
  dfs(0,0)

  for i in dp:
    print(i)
"""
 
print("40. 숨바꼭질")












