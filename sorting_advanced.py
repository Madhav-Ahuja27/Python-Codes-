lst=[32,5,41,51,15,12]
# # minInd=0
# # for i in range()




def insertionSort(nums):
  for i in range(1,len(nums)):
    temp=nums[i]
    j=i-1
    while j>=0 and temp<nums[j]:
      nums[j+1],nums[j]=nums[j],nums[j+1]
      j-=1
    nums[j+1]=temp
  return nums

Length=int(input("Enter length"))
nums=[]

for i in range(Length):
  inp=int(input(f"Enter number {i+1} :"))
  nums.append(inp)
print(insertionSort(nums))


# # nums=[9,2,4,56,15]
# # for i in range(1,len(nums)):
# #   temp=nums[i]
# #   j=i-1
# #   while j>=0 and temp<nums[j]: 
# #       nums[j],nums[j+1]=nums[j+1],nums[j]
# #       j-=1
# #   nums[j+1]=temp
    
# # print(nums)

##Bubble sort
# nums=[2,5,6,1,8,4]
# # for i in range(len(nums)):
# #   for j in range(len(nums)-i-1):
# #     if nums[j]>nums[j+1]:
# #       nums[j],nums[j+1]=nums[j+1],nums[j]
# # print(nums)

##Insertion sort
# for i in range(1,len(nums)):
#   temp=nums[i]
#   j=i-1
#   while j>=0 and temp<nums[j]:
#     nums[j],nums[j+1]=nums[j+1],nums[j]
#     j-=1
#   nums[j+1]=temp
# print(nums)

#Exchange sort
# nums=[5,1,4,2,8]
# for i in range(len(nums)-1):
#   for j in range(i+1,len(nums)):
#     if nums[i]>nums[j]:
#       nums[i],nums[j]=nums[j],nums[i]
# print(nums)


#merge sort is for large lists
##MERGE sort or divide and conque


# def sortmerge(left,right):
#   result=[]
#   i,j=0,0
#   while i<len(left) and j<len(right):
#     if left[i]<right[j]:
#       result.append(left[i])
#       i+=1
#     else:
#       result.append(right[j])
#       j+=1
#   result+=left[i:]
#   result+=right[j:]
#   return result

# def splitMerge(lst):
#   if len(lst)<=1:
#     return lst
#   else:
    
#     mid=len(lst)//2
#     left=splitMerge(lst[:mid])
#     right=splitMerge(lst[mid:])
#     sortmerge(left,right)





# nums=[38,27,43,3,9,82,10]

# splitMerge(nums)


# def merge(left,right):
#   sort = []
#   i,j=0,0
#   while i<len(left) and j<len(right):
#     if left[i] < right[j]:
#       sort.append(left[i])
#       i+=1
#     else:
#       sort.append(right[j])
#       j+=1
#   sort+= left[i:]
#   sort+= right[j:]
#   return sort


# def mergesort(nums):
#   if len(nums)<=1:
#     return nums
#   mid = len(nums)//2
#   left = mergesort(nums[:mid])
#   right = mergesort(nums[mid:])
#   return merge(left,right)

# nums = []
# n = int(input("enter the lenght of list: "))
# for i in range(n):
#   num = int(input(f"enter element {i+1}: "))
#   nums.append(num)
# result = mergesort(nums)
# print("The sorted list is ", resul


nums=[9,4,5,7,6,1,2]
#bubble sort
# for i in range(len(nums)-1):
#   for j in range(len(nums)-1-i):
#     if nums[j]>nums[j+1]:
#       nums[j],nums[j+1]=nums[j+1],nums[j]
# print(nums)

#selection sort
# for i in range(len(nums)-1):
#   minInd=i
#   for j in range(i+1,len(nums)):
#     if nums[minInd]>nums[j]:
#       minInd=j
#   nums[i],nums[minInd]=nums[minInd],nums[i]
# print(nums)

#insertion sort
for i in range(1,len(nums)):
  temp=nums[i]
  j=i-1
  while j>=0 and temp<nums[j]:
    nums[j],nums[j+1]=nums[j+1],nums[j]
    j-=1
  nums[j+1]=temp    
print(nums)

#exchange sort
# for i in range(len(nums)-1):
#   for j in range(i+1,len(nums)):
#     if nums[j]<nums[i]:
#       nums[i],nums[j]=nums[j],nums[i]
# print(nums)

#merge sort

def split(nums):
  if len(nums)<=1:
    return nums
  else:
    mid=len(nums)//2
    left=split(nums[:mid])
    right=split(nums[mid:])
    return merge(left,right)

def merge(left,right):
  sorted=[]
  i,j=0,0
  while i<len(left) and j<len(right):
    if left[i]<right[j]:
      sorted.append(left[i])
      i+=1
    else:
      sorted.append([j])
      j+=1
  sorted+=left[i:]
  sorted+=right[j:]
  return sorted
  






print(split(nums))
