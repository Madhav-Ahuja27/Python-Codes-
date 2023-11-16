# Linear search

# list1=[9,8,7,4,5,6]
# find=int(input("Enter the number to find:"))

# def linearSearch(list,key):
#   for i in range(len(list)):
#     if list[i]==key:
#       print(f"The number {key} is present and is on index {i}")
#       break
#   else:
#     print("The number was not in the list")

# linearSearch(list1,find)

#Binary search

list1 = [5, 65, 145, 1, 6, 55, 15, 18, 415, 48, 59, 4841, 85, 18]
list1.sort()
key = 5


# def binarySearch(list, key):
#   beg = 0
#   end = len(list1) - 1

#   while beg <= end:
#     mid = (end + beg) // 2
#     if list[mid] == key:
#       return mid
#     elif list[mid] < key:
#       beg = mid + 1
#     else:
#       end = mid - 1

#   return -1


# value = binarySearch(list1, key)
# print(value)






# def BS(lst,key):
#   beg=0
#   end=len(lst)-1
#   while beg<=end:
#     mid=(beg+end)//2
#     if lst[mid]==key:
#       return key
#     elif lst[mid]>key:
#       end=mid-1
#     else:
#       beg=mid+1
#   return -1

# print(BS(list1,5))
# lst=[]
# for i in range(5):
#   lst.append(int(input()))
# print(lst)

# dict={}
# for j in range(5):
#   dict[lst[j]]=input()
# print(dict)

N=[float (i) for i in input().split()]
print(list(set(N)))
