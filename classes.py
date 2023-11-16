from collections.abc import Iterable


class Student:
    def __init__(self,n,r,c):
        self.name=n
        self.rollno=r
        self.contact=c
    def __dir__(self):
        return(self.name)
    def printinfo(self):
        print(f"the name of the person is ")


# inp=input("Enter input")
# print(f"this is the input {inp}")
# def printthis():
#     print("this")


# if __name__=="__main__":    
#     inp=input("Enter input")
#     print(f"this is the input {inp}")
# def printthis():
#     print("this")

a=Student("thisname",77,708)
rv=a.__dir__()
print(rv)
