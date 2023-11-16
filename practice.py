# # l=[5,9,12,7,2]

# #Bubble sort

# # for i in range(len(l)-1):
# #   for j in range(len(l)-i-1):
# #     if l[j]>l[j+1]:
# #       l[j],l[j+1]=l[j+1],l[j]
# # print(l)

# #Selection sort

# # for i in range(len(l)-1):
# #   min=i
# #   for j in range(i+1,len(l)):
# #     if l[min]>l[j]:
# #       min=j
# #       l[min],l[i]=l[i],l[min]
      
# # print(l)

# #Insertion sort
# # for i in range(1,len(l)):
# #   temp=l[i]
# #   j=i-1
# #   while j>=0 and temp<l[j]:
# #     if l[j]>l[j+1]:
# #       l[j],l[j+1]=l[j+1],l[j]
# #     j-=1
# #   l[j+1]=temp
# # print(l)

# #exchange
# # for i in range(len(l)-1):
# #   for j in range(i+1,len(l)):
# #     if l[i]>l[j]:
# #       l[i],l[j]=l[j],l[i]
# # print(l)

# #merge

# l=[5,9,12,7,2]
# # def split(lst):
# #   if len(lst)<=1:
# #     return lst
# #   else:
# #     mid=len(lst)//2
# #     left=split(lst[:mid])
# #     right=split(lst[mid:])
# #     return merge(left,right)


# # def merge(left,right):
# #   sorted=[]
# #   i,j=0,0
# #   while i<len(left) and j<len(right):
# #     if left[i]<right[j]:
# #       sorted.append(left[i])
# #       i+=1
# #     else:
# #       sorted.append(right[j])
# #       j+=1
# #   sorted+=left[i:]
# #   sorted+=right[j:]
# #   return sorted


# # print(split(l))

# for i in range(len(l)-1):
#   for j in range(len(l)-i-1):
#     if l[j]>l[j+1]:
#       l[j],l[j+1]=l[j+1],l[j]
# print(l)

# for i in range(len(l)-1):
#   ind=i
#   for j in range(i,len(l)):
#     if l[ind]>l[j]:
#       ind=j
#       l[i],l[ind]=l[ind],l[i]
# print(l)

# for i in range(len(l)-1):
#   temp=l[i]
#   j=i-1
#   while j>=0 and temp<l[j]:
#     if l[j]>l[j+1]:
#       l[j],l[j+1]=l[j+1],l[j]
#   l[j+1]=temp

# print(l)

