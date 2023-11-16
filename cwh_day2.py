# x=6
# # y=9
# def f():
#     global x
#     global y
#     x=5
#     y=6

# f()
# print(x)
# print(y)

# class Person:
#     name="Madhav"
#     no=7087083079
#     add="F-1102"
#     roll=65
#     def info(self):
#         print(f"The name of the person is {self.name}, the name in lower case is {self.name.lower()}, the phone number is {self.no}, the address is {self.add}, and the roll number is {self.roll}")

# madhav=Person()
# madhav.info()

# lakshay = Person()
# lakshay.name="Lakshay"
# lakshay.no=7589490097
# lakshay.add="Adress idfk"
# lakshay.roll=64
# lakshay.info()

# Nikhil=Person()
# Nikhil.name="Manekas"
# Nikhil.info()


# import math

# print(math.sqrt(3)*math.pi)

# from interactive_system import calc
# calc(1,2,'+')

# def square(val):
#     return val*val

# rr=square(2)
# print(rr)

# cube=lambda v:v*v*v
# rx=cube(2)
# print(rx)

# class P2:
#     def __init__(self,nm,no):
#         self.name=nm
#         self.number=no
#     def info(self):
#         print(f"The name of the person is {self.name} and the roll number of the person is {self.number}")

# one=P2("madhav",65)
# two=P2("lakshay",64)
# one.info()
# two.info()

# class Parent(object):
#     def _init_(self,n,i):
#         self.name=n
#         self.id=i
#     def showinfo(self):
#         print(f"name is {self.name} and id is {self.id}")

# class Child(Parent):
#     def __init__(self,cn,add):
#         self.contact=cn
#         self.address=add
#     def info(self,name,id):
#         print(f"name is {self.name} and id is {self.id} also the contact is {self.contact} and the address is {self.address}")
# b=Child(7087083079,"F-1102")
# b.info("madhav",65)

# class Last:
#     name="Madhav"
#     __id=65
#     def info(self):
#         pass

# a=Last()
# print(a.name)
# print(a._Last__id)
# print(dir(a))


# class Parent():
#     name="madhav"
#     id=65
#     def info(self):
#         print(f"name is {self.name} and id is {self.id}")

# class Child(Parent):
#     def __init__(self,cn,add):
#         self.contact=cn
#         self.address=add
#     def info(self):
#         print(f"name is {self.name} and id is {self.id} also the contact is {self.contact} and the address is {self.address}")
# b=Child(7087083079,"F-1102")
# b.info()

# class newclass:
#     __name="madhav"

# b=newclass()


# print(b._newclass__name)
