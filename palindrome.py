str=input()
for i in range(len(str)):
    if str[0]==str[-1]:
        print(str) 
    else:
        i=0
        while str[0]!=str[-1]:
            str=str[0:len(str)-1-i]
            i-=1

print(str) 
