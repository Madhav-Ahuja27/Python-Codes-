# import numpy as np
# m1=np.array([[1,2,3],[4,5,6]])
# m2=np.array([[7,8],[9,10],[11,12]])


# if len(m1[0])!=len(m2):
#     print("multiplication of this matrix is not possible")
# else:
#     m3=[[0 for i in range(len(m2[0]))] for j in range(len(m1))]
# for i in range(len(m1)):
#     for j in range(len(m2[0])):
#         for k in range(len(m2)):
#             m3[i][j]+=m1[i][k]*m2[k][j]
# for r in m3:
#     print(r)

row=int(input())
col=int(input())
mat=[]
for i in range(row):
  mat.append([])
  for j in range(col):
    mat.append(int(input()))
for i in range(row-1):
  for j in range(col-1):
    print(mat[i][j],end="") 
