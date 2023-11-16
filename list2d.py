import numpy as n
# arr=numpy.array([[4,3],[3,1]])
# print(arr)
# arr2=numpy.matrix('4,3;2,1')
# print(arr2)

# for i in range(2):
#   for j in range(2):
#     print(arr[i][j])

# m3=n.array([[],[]])
m1=n.array([[4,3],[1,2]])
m2=n.array([[4,5],[9,10]])
for i in range(2):
  for j in range(2):
    print(m1[i][j]+m2[i][j],end=" ")
print()
print(n.add(m1,m2),end=" ")

#multiply two matrices

# import numpy as np


# matrix1 = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])

# matrix2 = np.array([
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ])


# result = matrix1 @ matrix2


# print(result)

#json means JavaScript Object Notation
# it means a text file written in any programming language used to store and transfer data
#python has an inbuilt package for json
#text in json is written in quoted string written in key value pairs within curly brackets
# a={"name":"madhav","rollno":65}
# print(type(a))
# import json
# result=json.dumps(a)
# print(result)
# print(type(result))

# list1=["Python","Programming"]
# print(type(list1))
# result2=json.dumps(list1)
# print(result2)
# print(type(result2))

# tup1=(1,2,3,4)
# print(type(tup1))
# result3=json.dumps(tup1)
# print(result3)
# print(type(result3))

# int1=65
# print(type(int1))
# r4=json.dumps(int1)
# print(r4)
# print(type(r4))

import json
a={"name":"madhav","rollno":65}
json_obj=json.dumps(a)
with open("sample.json",'a') as outfile:
  outfile.write(json_obj)

# 'a' is for append
# 'w' is for overriding data
