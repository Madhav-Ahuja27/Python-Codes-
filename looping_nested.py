list1=[1,2,3,4,5,6]
for i in list1:
  print(i)

st={"m":"a","a":"h","d":"u","h":"j","a":"a","v":"m"}
for i in st:
  print("%s,%s"%(i,st[i]))

for i in range(20):
  if i==10:
    break
  print(i)
  #sends control out of the loop and immediately executes the next statement

for i in range(20):
  if i==10:
    continue
  print(i)
  #retuens control to beginning of the loop

for i in range(1,5):
  for b in range(1,i+1):
    print(i,end="")
  print()
