

# def bubbleSort(arr):
# 	n = len(arr)
# 	swapped = False
# 	for i in range(n-1):
# 		for j in range(0, n-i-1):
# 			if arr[j] > arr[j + 1]:
# 				swapped = True
# 				arr[j], arr[j + 1] = arr[j + 1], arr[j]		
# 		if not swapped:
# 			return




# arr = []
# lenArr=int(input("Enter length of array"))
# for i in range(lenArr):
#     x=int(input(f"Enter element {i+1}"))
#     arr.append(x)

# bubbleSort(arr)

# print("Sorted array is:")
# for i in range(len(arr)):
# 	print("% d" % arr[i], end=" ")

def selectionSort(array, size):
	
	for ind in range(size):
		min_index = ind

		for j in range(ind + 1, size):
			if array[j] < array[min_index]:
				min_index = j
		(array[ind], array[min_index]) = (array[min_index], array[ind])


arr = []
lenArr=int(input("Enter length of array"))
for i in range(lenArr):
    x=int(input(f"Enter element {i+1}:"))
    arr.append(x)
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
