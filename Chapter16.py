"""
print("31. 금광")

from collections import deque

def check(dp,n,m,N):
  x=0
  print(n,m)
  if n==0:
    x=max(dp[n+1][m-1],dp[n][m-1])
  elif n==N:
    x=max(dp[n][m-1],dp[n-1][m-1])
  else:
    x=max(dp[n+1][m-1],dp[n][m-1],dp[n-1][m-1])

  x=x+graph[n][m]
  
  return x


t=int(input())
for _ in range(t):
  n,m=map(int,input().split())
  graph=[[0]*m for _ in range(n)]
  q=deque(list(map(int,input().split())))
  for i in range(n):
    for j in range(m):
      graph[i][j]=q.popleft()
  dp=[[0]*m for _ in range(n)]
  for i in range(n):
    dp[i][0]=graph[i][0]
  for i in range(n):
    print(graph[i])
  print()
  for i in range(n):
    print(dp[i])
  print()
  

  for i in range(1,m):
    for j in range(n):
      dp[j][i]=check(dp,j,i,n)
      
      for i in range(n):
        print(dp[i])
      print()
  


"""
print("32. 정수 삼각형")

n=int(input())
dp=[0]*n
now=[0]*n

for i in range(n):
  nlist=list(map(int,input().split()))
  for j in range(len(nlist)):
    if j==0:
      now[j]=dp[j]+nlist[j]
    elif j==len(nlist):
      now[j]=dp[j-1]+nlist[j]
    else:
      now[j]=max(dp[j-1],dp[j])+nlist[j]
  dp=now[:]
      
print(max(dp))