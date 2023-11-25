def smol(lst):
  smallest=lst[0]
  for i in lst:
    if smallest>i:
      smallest=i
  return smallest
lst=[]
for i in range(10):
  lst.append(int(input()))
smallest=smol(lst)
print(smallest)
lst.remove(smallest)
secsmol=smol(lst)
print(secsmol)
