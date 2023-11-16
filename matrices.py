import numpy as np
mat1=np.array([[1,2],[2,4]])
print(mat1)

mat2=np.array([[1,0],[0,1]])
print(mat2)
mat3=np.add(mat1,mat2)
print(mat3)

det=np.linalg.det(mat2)
print(det)
print(np.dot(mat2,mat3))

inverse=np.linalg.inv(mat2)
print(inverse)
