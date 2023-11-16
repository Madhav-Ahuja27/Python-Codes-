# # def greet(fx):
# #     def mfx(*args,**kwargs):
# #         print("first")
# #         fx(*args,**kwargs)
# #         print("last")
# #     return mfx


# # @greet
# # def add(a,b):
# #     print(a+b)

# # add(1,2)

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("ok")
#         fx(*args,**kwargs)
#         print("bro")
#     return mfx

# @greet
# def fd(a,b):
#     print(a//b)
# fd(5,2)

class company():
    companyname="apple"
    @classmethod
    def ccname(cls,n):
        cls.companyname=n

print(company.companyname)
a=company()
a.ccname('notapple')
print(company.companyname)
