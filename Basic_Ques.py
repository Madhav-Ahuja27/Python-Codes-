# a=[1,2,3,4,5,6]
# i=0
# no=a[0]
# while i<len(a):
#     if no>a[i]:
#         no=a[i]
#         i+=1
# print(no)

# str=input()


# def bro(str):
#     i=0
#     while i <= len(str):
#         if str[i]==str[-i-1]:
#             return True
#         else:
#             return False
#         i+=1
# x=bro(str)
# print(x)

# x=10
# y=20
# x,y=y,x
# print(x,y)

# year=int(input())
# if year % 400 ==0 and year % 100 == 0:
#     print("Leap year")
# elif year % 4 == 0 and year % 100 != 0:
#     print("leap year")
# else:
#     print("Not Leap Year")

# num=int(input())
# if num==1:
#     print("Not prime")
# elif num==0:
#     print("Not prime")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("Not prime")
#             break
#     else:
#         print("Prime")

# lower=int(input())
# upper=int(input())
# for i in range(lower,upper+1):
#     if i>1:
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             print(i)

# num=int(input())
# fact=1
# for i in range(1,num+1):
#     fact=fact*i
# print(fact)

# a=0
# b=1
# c=0
# n=int(input())
# if n==1:
#     print(a)
# else:
#     print(a)
#     print(b)
#     for i in range(n):
#         c=a+b
#         print(c)
#         a,b=b,c

# num=int(input())
# fact=1
# i=1
# while i < num:
#     fact=fact*i
#     i+=1
# print(fact)

# a=input()
# rev=a[::-1]
# if a==rev:
#     print("Yes")
# else:
#     print("No")

# [int (i) for i in input().strip()]

bro1=[float (i) for i in range(1,11) if i%2==0]
print(bro1)

bro1=[float (i) for i in range(1,11) if i%2!=0]
print(bro1)
