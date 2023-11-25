inp=int(input())
lst=[]
for i in range(inp):
  lst.append(input())
newinp=input()
if newinp in lst:
  print("Name found")
else:
  lst.append(newinp)
  print(lst)
dic={}
for i in range(10):
  x=input()
  if x not in dic:
    dic[x]=0
  dic[x]+=1
for j in dic:
  print(f"{j} : {dic[j]}")
