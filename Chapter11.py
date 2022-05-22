"""
print("01. 모험가 길드")

n=int(input())
nlist=list(map(int,input().split()))
nlist.sort()
count=0

while nlist:
  print(count,":",nlist)
  x=nlist.pop(0)
  for _ in range(x-1):
    if not nlist:
      print(count)
      exit()
    nlist.pop()
  count+=1
print(count)
"""  
"""
print("02. 곱하기 혹은 더하기")

s=""
s=input()
answer=0
for i in s:
  x=int(i)
  if answer+x>answer*x:
    answer=answer+x
  else:
    answer=answer*x
print(answer)
"""
"""
print("03. 문자열 뒤집기")

s=""
s=input()
ary=[]
cnt=0
for i in range(1,len(s)):
  if s[i-1]==s[i]:
    continue
  ary.append(s[i-1])
  cnt+=1
if s[-1]!=s[-2]:
  ary.append(s[-1])
  
print(len(ary)//2)
"""
"""
print("04. 만들 수 없는 금액")
import sys 
sys.setrecursionlimit(10 ** 6)

def dfs(x,sum):
  if visited[x]==True:
    return
  visited[x]=True
  if sum>MAX:
    return
  dp[sum]=True
  for i in range(x,len(ary)):
    dfs(i,sum+ary[i])
    visited[i]=False
    
MAX=1000001
n=int(input())
ary=list(map(int,input().split()))
visited=[False]*(n+1)
dp=[False]*MAX
dp[0]=True
#ary.sort()

for i in range(n):
  dfs(i,ary[i])

for i in range(30):
  print(i,dp[i])

for i in range(MAX): 
  if dp[i]==False:
    print(i)
    break
"""
"""
print("05. 볼링공 고르기")

n,m=map(int,input().split())

arr=list(map(int,input().split()))
cnt=0

for i in range(len(arr)):
  for j in range(i,len(arr)):
    if arr[i]==arr[j]:
      continue
    cnt+=1
print(cnt)
"""
"""
print("06. 무지의 먹방 라이브")
#효율성 이외 성공
def solution(food_times, k):
    idx = 0
    answer = -1
    sw=False
    n = len(food_times)
    
    #효율성
    if sum(food_times)<=k:
        return -1
    m=min(food_times)
    if m*n <=k:
        k-=m*n
        for i in range(n):
            food_times[i]-=m
    print(food_times)
    
    #문제풀이
    for i in range(k):
        while food_times[idx] == 0:
            if sum(food_times) <= 0:
                sw=True
                break
            idx+=1
            if idx>=n:
                idx-=n
        if sw==True:
            break
        
        food_times[idx]-=1
        idx+=1
        if idx>=n:
            idx-=n
        
    if sum(food_times) <= 0:
        return -1
    while food_times[idx] == 0:
        idx+=1
        if idx>=n:
            idx-=n
    answer=idx+1
    
    return answer
"""

print("06. 무지의 먹방 라이브")
#효율성 이외 성공




























