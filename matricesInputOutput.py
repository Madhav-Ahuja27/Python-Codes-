matrix=[]
rows=int(input("enter number of rows"))
cols=int(input("enter number of cols"))
for i in range(rows):
  a=[]
  for j in range(cols):
    a.append(int(input()))
  matrix.append(a)

print("[",end="")
for i in range(rows):
  for j in range(cols):
    print(matrix[i][j],end=" ")
  if i!=rows:
    print()
print("]",end="")
matrix=[]
for i in r:
  a=[]
  for j in c:
    a.append(int(input()))
  matrix.append()

a=2
b=5
print("a>b") if a>b else print("a=b") if a==b else print("a<b")

import numpy as np
B=[[1,8,9],[2,5,0],[4,6,3]]
print(B)
A=[]
for i in range(3):
  a=[]
  for j in range(3):
    a.append(int(input()))
  A.append(a)
print(A)
for i in range(3):
  print(np.add(A[i],B[i]))
