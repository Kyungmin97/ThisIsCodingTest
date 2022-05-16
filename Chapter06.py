"""
print("02. 위에서 아래로")

n=int(input())
nlist=[]
for _ in range(n):
  nlist.append(int(input()))
nlist.sort(reverse=True)
print(nlist)
"""

"""
print("03. 성적이 낮은 순서로 학생 출력하기")

def keys(nlist):
  return nlist[1]

n=int(input())
nlist=[]
for i in range(n):
  nlist.append(input().split())
print(nlist)
print(sorted(nlist,key=keys))
print(sorted(nlist,key=lambda _:nlist[1],reverse=True))
"""

print("04. 두 배열의 원소 교체")

n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(a,b)
for _ in range(k):
  a[a.index(min(a))],b[b.index(max(b))]=b[b.index(max(b))],a[a.index(min(a))]
  print(a,b)
print(sum(a))




























































