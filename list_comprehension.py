# list1=["python","calculus","linear algebra","ai"]
# list2=[y if y != "ai" else "cms" for y in list1]
# # print(list2)
# list1=["python","calculus","linear algebra","ai"]
# list2=[y.upper()  for y in list1 if y != "python"]
# print(list2)

a=[[1,2,3,4],[2,3,4,5],[6,7,8,9],[7,8,9]]
for i in a:
    for j in i:
        print("[",j,"]",end="")
    print()

# A jacked array in python is an array of arrays where the sub arrays can have varying lengths.

# # x=int(input())
# # y=int(input())
# # z=int(input())
# # q=int(input())
# # t=int(input())
# # i=int(input())
# # lst=[]
# # lst.append

# # kalra=[int (i) for i in input().split()]
# # print(kalra)

# def merge_the_tools(string, k):
#   # your code goes here
#   n=len(string)
#   x=int(n/k)
#   s1=string[:x+1]
#   s2=string[x:(x+x)+1]
#   s3=string[(x+x):(x+x+x)+1]
#   s11,s22,s33="","",""
#   for i in s1:
#     if i not in s11:
#           s11+=i
#   for i in s2:
#     if i not in s11:
#           s22+=i
#   for i in s3:
#     if i not in s11:
#           s33+=i
#   print(s11)
#   print(s22)
#   print(s33)




# if __name__ == '__main__':
#   string, k = input(), int(input())
#   merge_the_tools(string, k)

import copy
lst=[1,2,3,4]
lst2=copy.deepcopy(lst)
print(lst,lst2)
