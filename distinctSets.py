import math
def subsets(A,n):
  return 1<<n


A=[1,2,2]
A=set(A)
n=len(A)
print(subsets(A,n))
