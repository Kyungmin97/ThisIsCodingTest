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

print("09. 문자열 압축")








