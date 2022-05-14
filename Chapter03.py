
"""
print("02. 큰 수의 법칙")

n,m,k=map(int,input().split())
nlist=list(map(int,input().split()))
nlist.sort()
print(nlist)
cnt=0
answer=0
for i in range(m):

  if cnt==k:
    cnt=0
    print(nlist[-2],end=' ')
    answer+=nlist[-2]
    continue
  
  print(nlist[-1],end=' ')
  answer+=nlist[-1]
  cnt+=1

print()
print(answer)
"""  

"""
print("03. 숫자 카드 게임")

n,m=map(int,input().split())
nlist=[]
for i in range(n):
  nlist.append(list(map(int,input().split())))
    
print(nlist)
answers=[]
for i in nlist:
  answers.append(min(i))
print(max(answers))
"""

print("04. 1이 될 때까지")

n,k=map(int,input().split())
cnt=0
while n!=1: 
  cnt+=1
  if n//k==n/k:
    n=n//k
  else: 
    n=n-1


print(cnt)

















