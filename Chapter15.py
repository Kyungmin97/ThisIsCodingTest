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









































