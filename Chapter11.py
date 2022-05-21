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
print("02. 곱하기 혹은 더하기")









