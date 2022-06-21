"""
print("23. 국영수")

n=int(input())
student=[]
for _ in range(n):
  a,b,c,d=map(str,input().split())
  student.append([a,int(b),int(c),int(d)])

student.sort(key=lambda x:x[0])
student.sort(key=lambda x:x[3],reverse=True)
student.sort(key=lambda x:x[2])
student.sort(key=lambda x:x[1],reverse=True)
for i in range(n):
  print(student[i][0])
"""
"""
print("24. 안테나")

n=int(input())
arr=list(map(int,input().split()))
arr.sort()

mid=(n-1)//2
print(arr[mid])


"""
"""
print("25. 실패율")

def solution(N, stages):
    fail = [0]*(N+2)
    answer = []
    nlist=[]
    numPeople=len(stages)
    
    for stage in stages:
        for i in range(1,stage):
            fail[i]+=1
    for i in range(1,N+1):
        fail[i]=numPeople-fail[i]
    for i in range(1,N+1):
        nlist.append([(fail[i]-fail[i-1])/(numPeople-fail[i-1]),i])
    
    
    nlist=sorted(nlist,key=lambda x:x[0],reverse=True)
    for i in nlist:
        answer.append(i[1])
        
    return answer
"""













