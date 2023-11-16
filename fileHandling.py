# import csv


# def writer():
#   with open("text.csv","w") as file:
#     write=csv.writer(file)
#     write.writerow(['ok','bro','this','is','a','new','file'])
#     data=[[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19,20]]
#     write.writerows(data)
# if __name__=="__main__":
#   writer()
# def reader():
#   with open("text.csv","r") as file:
#     read=csv.reader(file)
#     for row in read:
#       print(row)
# if __name__=="__main__":
#   reader()

#   def appender():
#     with open("txt.csv","a",newline="") as file:
#       write=csv.writer(file)
#       # write.writerow(" ")
#       write.writerow(['ok','bro','this','is','a','new','file'])
#   if __name__=="__main__":
#     appender()



# file=open("text.csv","w")
# write=csv.writer(file)
# write.writerow(['ok','bro','this','is','a','new','file'])
# data=[[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19,20]]
# write.writerows(data)
  
# file=open("text.csv","r")
# read=csv.reader(file)
# for row in read:
#   print(row)
# file.close()

  
  
  
  
  
  
  
  
  
  
    # print(read)

# def appender():
#   fields=["name","class","grp"]
#   with open("text.csv","a",) as file:
#     write=csv.DictWriter(file,fieldnames=fields)
#     data=[{"class":"0","name":"m","grp":"b"}]
#     write.writerows(data)
# if __name__=="__main__":
#   appender()
# def reader():
#   with open("text.csv","r") as file:
#     read=csv.reader(file)
#     for row in read:
#       print(row)
# if __name__=="__main__":
#   reader()

# import json
# def writer():
#   with open("text.csv","w") as file:
#     write=json.dump(file,'w')
#     write.writerow(['ok','bro','this','is','a','new','file'])
#     data=[[1,2,3,4,5,6,7,8,9],[10,11,12,13,14,15,16,17,18,19,20]]
#     write.writerows(data)
# if __name__=="__main__":
#   writer()
# def reader():
#   with open("text.csv","r") as file:
#     read=json.load(file)
#     for row in read:
#       print(row)
# if __name__=="__main__":
#   reader()
