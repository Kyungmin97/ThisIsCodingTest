"""
print("02. 1로 만들기")

n=int(input())
dp=[0]*30000+1
array=[]
cnt=0
array.append(n)
while True:
  n=array.popleft()
  if n%5==0:
   dp[n//5]=n//5
  if n%3==0:
   dp[n//3]=n//3
  if n%2==0:
   dp[n//2]=n//2
  dp[n-1]=n-1
"""  
"""
print("03. 개미 전사")

def ant(now):
  end=len(array)
  if now==end or now==end-1:
    return
  
  for i in range(now+2,end):
    dp[i]=max(dp[i],dp[now]+array[i])
    ant(i)

n=int(input())
array=list(map(int,input().split()))
dp=[0]*1001
dp[0],dp[1]=array[0],array[1]
ant(0)
ant(1)
print(dp[n])
print(n,array,dp[:10])
"""  

"""   
print("04. 바닥 공사")

n=int(input())
dp=[0]*1001
dp[1]=1
dp[2]=3
dp[3]=5
dp[4]=11
dp[5]=21
for i in range()
"""

"""
print("05. 효율적인 화폐 구성")


n,m=map(int,input().split())
array=[]
for _ in range(n):
  array.append(int(input()))
dp=[10001]*(m+1)
dp[0]=0

for i in range(n):
  for j in range(array[i],m+1):  
    if dp[j-array[i]] != 10001:
      dp[j]=min(dp[j],dp[j-array[i]]+1)

if dp[m] == 10001:
  print(-1)
else:
  print(dp[m])
"""








































