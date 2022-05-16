"""
print("01. 이진 탐색 코드 BASIC")

def binary(array,target,start,end):
  if start>end:
    return None
  mid=(start+end)//2
  if array[mid]==target:
    return mid
  elif array[mid]>target:
    return binary(array,target,start,mid-1)
  else:
    return binary(array,target,mid+1,end)

n,target=list(map(int,input().split()))
"""
"""
print("01. 이진 탐색 코드 BASIC")
import sys
x=sys.stdin.readline()
print(x)
y=sys.stdin.readline().rstrip()
print(y)
"""

"""
print("02. 부품 찾기")

import sys
n=int(sys.stdin.readline().rstrip())
nlist=list(map(int,sys.stdin.readline().rstrip().split()))
m=int(sys.stdin.readline().rstrip())
mlist=list(map(int,sys.stdin.readline().rstrip().split()))
nlist.sort()

def search(target,start,end):
  mid=(start+end)//2

  if start>end:
    return None
  if target==nlist[mid]:
    return True
  if target>nlist[mid]:
    return search(target,mid+1,end)
  if target<nlist[mid]:
    return search(target,start,mid-1)

for i in mlist:
  print("Yes" if search(i,0,len(nlist)) else "No", end=' ')
"""
"""
print("03. 떡볶이 떡 만들기")

n,m=map(int,input().split())
nlist=list(map(int,input().split()))
h=max(nlist)

while True:
  x=0
  for i in nlist:
    y=i-h
    if y>0:
      x+=y
  if x>=m:
    print(h)
    break
  h-=1
"""





























