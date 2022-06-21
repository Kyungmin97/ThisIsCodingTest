"""
print("27. 정렬된 배열에서 특정 수의 개수 구하기")

n,x=map(int,input().split())
arr=list(map(int,input().split()))

def numcount(mid,target):
  print("numcount:",mid,target)
  cnt=1
  cnt2=1
  while True:
    if arr[mid+cnt]==target:
      cnt+=1
    elif arr[mid-cnt2]==target:
      cnt2+=1
    else:
      return cnt+cnt2-1
  
def binary_search(start,end,target):
  print("binary_search",start,end,target)
  if end<=start:
    return -1
  mid=(start+end)//2
  if arr[mid]==target:
    return numcount(mid,target)
  if arr[mid]>target:
    return binary_search(start,mid,target)
  elif arr[mid]<target:
    return binary_search(mid+1,end,target)
    
print(binary_search(0,n,x))
"""
"""
print("28. 고정점 찾기")

#O(N)?
n=int(input())
cnt=0
for i in map(int,input().split()):
  if cnt==i:
    print(i)
    exit()
  cnt+=1
print(-1)

#O(logN)
def search(min,max):
  mid=(min+max)//2
  print(min,mid,max)
  if min>max:
    return -1
    

  if mid>nlist[mid]:
    return search(mid+1,max)
  elif mid<nlist[mid]:
    return search(min,mid-1)
  elif mid==nlist[mid]:
    return mid


n=int(input())
nlist=list(map(int,input().split()))
print(search(0,n-1))
"""

  
  







































