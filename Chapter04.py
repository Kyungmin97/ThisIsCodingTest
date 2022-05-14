"""
print("02. 왕실의 나이트")

n=str(input())
x,y=ord(n[0])-ord('a'),int(n[1])-1
print("x,y:",x,y)

dx=[2,2,1,1,-1,-1,-2,-2]
dy=[1,-1,2,-2,2,-2,1,-1]

cnt=0

for i in range(8):
  nx,ny=x+dx[i],y+dy[i]
  if nx<0 or ny<0 or nx>7 or ny>7:
    continue
  print("Target: ",chr(nx+ord('a')),ny+1)
  cnt+=1

print(cnt)
"""

print("03. 게임 개발")

n,m=map(int,input().split())
x,y,d=map(int,input().split())
nlist=[]
answer=1

dx=[0,-1,0,1]
dy=[-1,0,1,0]

for _ in range(n):
  nlist.append(list(map(int,input().split())))
  
nlist[y][x]=2
d=d+1
sw=True

while True:
  for i in range(4):
    if d<=0:
      d=d+4
    d-=1
  
    nx,ny=x+dx[d],y+dy[d]
    if nx<0 or ny<0 or nx>=m or ny>=n:
      continue
    if nlist[ny][nx]>0:
      continue
  
    answer+=1
    print(nx,ny,d)
    x,y=nx,ny
    nlist[y][x]=2
    sw=False
    break
    
  if sw==True:
    if d<=0:
      d=d+4
    d-=1
    nx,ny=x-dx[d],y-dy[d]
    
    if nx<0 or ny<0 or nx>=m or ny>=n:
      break
    if nlist[ny][nx]==1:
      break
    x,y=nx,ny
  sw=True

for i in nlist:
  print(i)
print(answer)

  

























