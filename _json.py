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
