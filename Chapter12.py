"""
print("07. 럭키 스트레이트")

s=""
s=input()
half=len(s)//2
sum1=0
for i in s[:half]:
  sum1+=int(i)

for i in s[half:]:
  sum1-=int(i)

if sum1==0:
  print("LUCKY")
else:
  print("READY")
"""
"""
print("08. 문자열 재정렬")

s=""
s2=[]
s=input()
sum=0
for i in s:
  if i >='0' and i<='9':
    sum+=int(i)
  else:
    s2.append(i)
s2.sort()
print(''.join(s2),end=str(sum))
"""
"""
print("09. 문자열 압축")

def check(s,size):
    answer = len(s)
    dif=len(s)//size
    arr=[]
    for i in range(dif):
        arr.append(s[i*size:(i+1)*size])
    if s[dif*size:] != '':
        arr.append(s[dif*size:])
    print(arr)
    
    
    
    return answer
    

def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        answer=min(answer,check(s,i))
    
    
    
    return answer
"""
"""
print("10. 자물쇠와 열쇠")
import copy

def check(a,b):
    arr2=copy.deepcopy(arr)
    for i in range(m):
        for j in range(m):
            arr2[i+m][j+m]+=key[i][j]
            if arr2[i+m][j+m]>1:
                return False
    for i in range(m):
        for j in range(m):
    
    return True

def solution(key, lock):
    answer = True
    n=len(lock)
    m=len(key)
    print(n,m)    
    arr=[[0]*(n*3) for _ in range(n*3)] 
    
    for i in range(n):
        for j in range(n):
            arr[i+n][j+n]=lock[i][j]
    
    print(arr)
    
    for i in range(3*n):
        for j in range(3*n):
            check(i,j)
    
    return answer
"""
"""
print("11. 뱀")

#우하좌상
dx=[1,0,-1,0]
dy=[0,1,0,-1]
n=int(input())
k=int(input())
x,y=1,1
apple=[]
board=[[0]*(n+1) for _ in range(n+1)]
dir=0
flag=True
for _ in range(k):
  apple.append(list(map(int,input().split())))
l=int(input())
answer=0
tail=0
tails=[]
for _ in range(l):
  n1,n2=map(str,input().split())
  n1=int(n1)
  if n2=='D':
    dir+=1
  else:
    dir-=1
  if dir>3:
    dir-=3
  if dir<0:
    dir+=3

  for _ in range(n1):
    x+=dx[dir]
    y+=dy[dir]
    answer+=1
    print(x,y)
    if x<1 or y<1 or x>=n or y>=n:
      flag=False
      break
    for i in tails:
      if x==i[0] and y==i[1]:
        flag=False
        break
    if flag==False:
      break
  
    if [x,y] in apple:
      apple.remove([x,y])
      tail+=1
    if tail>0:
      tails.append([x,y,tail])
    for i in tails:
      i[2]-=1
      if i[2]<0:
        tails.remove(i)
  if flag==False:
    break
print(answer)
"""
print("12. 기둥과 보 설치")












