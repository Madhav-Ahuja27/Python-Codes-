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
