# Write a function to find the first non-repeating character in a string while treating both uppercase and lowercase characters as equal. It also states if there is no any non-repeating character in the string.

str1=input().lower()
flag=False
for i in str1:
  if str1.count(i)==1:
    print(str1.index(i))
    flag=True
    break
  else:
    continue
if flag==False:
  print("no non repeating character")
