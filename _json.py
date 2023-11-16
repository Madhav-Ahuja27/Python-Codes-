# import json
# a={"name":"madhav","rollno":65}
# json_obj=json.dumps(a)
# with open("sample.json","w") as outfile:
#   outfile.write(json_obj)

# f=open("sample.json")
# data=json.load(f)
# for i in data:
#   print(i,data[i])
# f.close()

import json
a={"name":"madhav","roll":65,"sub":"ai"}
json_temp=json.dumps(a)
with open("new","w") as file:
    file.write(json_temp)
    
opener=open("new.json")
data=json.load(opener)
for i in data:
    print(i,data[i])

# '''JavaScripts Object Notation
# Key value pairs(dicts) [list of]'''
#but json takes list of dictionaries
# import json
# data={'name':'madhav','year':1,'grp':'B'}
# data2={'name':'madhav2','year':2,'grp':'A'}
# data3={'name':'madhav3','year':3,'grp':'C'}
# with open('file.json','w') as file:
#   json.dump([data,data2,data3],file, indent=4,separators=("; "," is equal to "),sort_keys=False)

# with open('file.json') as file:
#   json.loads(file)

# dict={}
# def dictGet(inp):
  
  
#   while inp!="n":
#     dictGet(inp)


# inp=input("Enter y/n")
# if inp=="y":
#   dictGet(inp)



# def Input(inp,dict):
#   if inp!="n" and inp=="y":
#     dict2={}
#     name=input("enter name:")
#     clas=input("enter class:")
#     grp=input("enter group:")
#     dict2['name']=name
#     dict2['class']=clas
#     dict2['group']=grp
#     dict=(dict | dict2)
#     print("Values added successfully")
#     Input(input("Enter y/n:"),dict)
    
# dict={}
# Input(input("Enter y/n:"),dict)
# print(dict)


# dict1={'name':'madhav','year':1,'grp':'B'}
# dict2={'name':'mxyv2','year':2,'grp':'A'}
# print(dict1 | dict2)

def Input(inp,lst):
  if inp!="n" and inp=="y":
    dict={}
    name=input("enter name:")
    clas=input("enter class:")
    grp=input("enter group:")
    dict['name']=name
    dict['class']=clas
    dict['group']=grp
    lst.append(dict)
    print("Values added successfully")
    Input(input("Enter y/n:"),lst)

lst=[]

Input(input("Enter y/n:"),lst)
print(lst)
import json
with open('file.json','w') as file:
  json.dump(lst,file, indent=4,separators=("; "," is equal to "),sort_keys=False)
