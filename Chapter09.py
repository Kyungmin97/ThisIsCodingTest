"""
print("다익스트라 연습 part 1")

#import sys
#input=sys.stdin.readline
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)
for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a].append((b,c))
  
def get_smallest():
  min_value=INF
  index=0
  for i in range(1,n+1):
    if distance[i]<min_value and not visited[i]:
      min_value=distance[i]
      index=i
  return index

def dijkstra(start):
  distance[start]=0
  visited[start]=True
  for j in graph[start]:
    distance[j[0]]=j[1]
  for i in range(n-1):
    now=get_smallest()
    visited[now]=True
    for j in graph[now]:
      cost=distance[now]+j[1]
      if cost<distance[j[0]]:
        distance[j[0]]=cost

dijkstra(start)

for i in range(1,n+1):
  if distance[i]==INF:
    print("INF")
  else:
    print(distance[i])
"""      

"""
print("다익스트라 연습 part 2")

import heapq
INF=int(1e9)

n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

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
    print("무한")
  else:
    print(distance[i])
      
"""
"""
print("플로이드 워셜 알고리즘 연습")

INF=int(1e9)

n=int(input())
m=int(input())
graph=[[INF]*(n+1) for i in range(n+1)]

for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for _ in range(m):
  a,b,c=map(int,input().split())
  graph[a][b]=c

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

for a in range(1,n+1):
  for b in range(1,n+1):
    if graph[a][b]==INF:
      print("무한",end=" ")
    else:
      print(graph[a][b], end=" ")
  print()
"""
"""
print("02. 미래 도시")
INF=int(1e3)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for i in range(n+1)]
for _ in range(m):
  a,b=map(int,input().split())
  graph[a][b]=1
  graph[b][a]=1
x,k=map(int,input().split())

##
for a in range(1,n+1):
  for b in range(1,n+1):
    if a==b:
      graph[a][b]=0

for k in range(1,n+1):
  for a in range(1,n+1):
    for b in range(1,n+1):
      graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])
distance=graph[1][k]+graph[k][x]

for i in graph:
  print(i)

if distance>=INF:
  print(-1)
else:
  print(distance)
"""

print("03. 전보")

import sys
import heapq
input=sys.stdin.readline
INF=int(1e3)

n,m,c=map(int,input().split())
graph=[[]*(n+1) for i in range(n+1)]
distance=[INF]*(n+1)
for _ in range(m):
  x,y,z=map(int,input().split())
  graph[x].append((y,z))

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

dijkstra(c)

count=0
max_distance=0
for d in distance:
  if d!=INF:
    count+=1
    max_distance=max(max_distance,d)
print(count-1,max_distance)

























